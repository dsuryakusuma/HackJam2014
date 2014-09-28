// adapted from http://jsfiddle.net/2nhTD/
var pat_id;
var width;
var height;
var color;
var svg;

window.onload = function() {
    pat_id = getURLParameter("pat_id");
    width = 800, height = 600;
    color = d3.scale.category20();
    svg = d3.select("body").append("svg").attr("width", width).attr("height", height);
    var graph = {
      "nodes": [
        {"name": "stkbl0001", "group": 1},
        {"name": "stkbl0002", "group": 1},
        {"name": "stkbl0003", "group": 1},
        {"name": "stkbl0004", "group": 1},
        {"name": "stkbl0005", "group": 1}
      ],
      "links": [
        {"source": "stkbl0001", "target": "stkbl0005", "value": 3},
        {"source": "stkbl0002", "target": "stkbl0005", "value": 3},
        {"source": "stkbl0003", "target": "stkbl0005", "value": 3},
        {"source": "stkbl0004", "target": "stkbl0005", "value": 3}
      ]};

    $.ajax({
        url: "/ajax/graph/?pat_id=" + encodeURIComponent(pat_id)
    }).done(showGraph);
}

function showGraph(jqXHR, textStatus) {
    if(textStatus != 'success') {
        alert("Error loading graph data.");
        return;
    }

    graph = {
        "nodes": [{"name": pat_id, "group": 1}],
        "links": []
    }
    nodes = {}
    parseGraph(graph, nodes, jqXHR.results, pat_id);
    
    var force = d3.layout.force().charge(-120).linkDistance(30).size([width, height]);

    var nodeMap = {};

    graph.nodes.forEach(function(d) { nodeMap[d.name] = d; });

    graph.links.forEach(function(l) {
        l.source = nodeMap[l.source];
        l.target = nodeMap[l.target];
    })

    force.nodes(graph.nodes)
        .links(graph.links)
        .start();

    var link = svg.selectAll(".link")
        .data(graph.links)
        .enter().append("line")
        .attr("class", "link")
        .style("stroke-width", function(d) {
            return Math.sqrt(d.value)+1;
        });

    var node = svg.selectAll(".node")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("class", "node")
        .attr("r", 5)
        .style("fill", function(d) { return color(d.group); })
        .call(force.drag);


      node.append("title")
      .attr("dx", 12)
      .attr("dy", ".35em")
      .text(function(d) { return d.name });

    node.on("click", function(e){ alert(nodes[e.name]) });

    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });
    });
};

function parseGraph(graph, nodes, json, child_pat_id) {
    for(var pat_id in json) {
        nodes[pat_id] = json[pat_id]['title']
        graph['nodes'].push({"name": pat_id, "group": 1})
        graph['links'].push({"source": pat_id, "target": child_pat_id, "value": 3})
        if("references" in json[pat_id]) {
            parseGraph(graph, nodes, json[pat_id]["references"], pat_id);
        }
    }
};

// from http://stackoverflow.com/questions/11582512/how-to-get-url-parameters-with-javascript/11582513#11582513
function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
};