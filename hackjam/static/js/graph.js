// adapted from http://jsfiddle.net/2nhTD/
window.onload = function() {
    var width = 800, height = 600;
    var color = d3.scale.category20();
    var svg = d3.select("body").append("svg").attr("width", width).attr("height", height);
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

    $.ajax("/ajax/graph/?pat_id=" + encodeURIComponent(getURLParameter("pat_id")), complete=showGraph);
}

function showGraph(jqXHR, textStatus) {
    if(textStatus != 'success') {
        alert("Error loading graph data.");
        return;
    }

    alert("done");
    alert(jqXHR.response);

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
        .text(function(d) { return d.name; });

    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });
    });


    function getData() {

      return {
      "nodes":[
        {"name":"stkbl0001","group":1},
        {"name":"stkbl0002","group":1},
        {"name":"stkbl0003","group":1},
        {"name":"stkbl0004","group":1},
        {"name":"stkbl0005","group":1}
      ],
      "links":[
        {"source":"stkbl0001","target":"stkbl0005","value":3},
        {"source":"stkbl0002","target":"stkbl0005","value":3},
        {"source":"stkbl0003","target":"stkbl0005","value":3},
        {"source":"stkbl0004","target":"stkbl0005","value":3}
      ] };    
        
    }
};

// from http://stackoverflow.com/questions/11582512/how-to-get-url-parameters-with-javascript/11582513#11582513
function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}