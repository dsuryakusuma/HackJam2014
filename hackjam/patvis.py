from flask import Flask, render_template, request, jsonify
from keyword_search import key_word_search_result as keyword_search

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/keywordsearch/')
def keywordsearch():
    query = request.args.get('query')
    if query:
        results = keyword_search(query, 10)
        results = [{'pat_id': result[0], 'title': result[1]} for result in results]
    else:
        results = None
    return render_template('keywordsearch.html', results=results)

@app.route('/graph/')
def graph():
    pat_id = request.args.get('pat_id', type=str)
    return render_template('graph.html', pat_id=pat_id)

@app.route('/ajax/graph/', methods=['GET'])
def ajax_graph():
    pat_id = request.args.get('pat_id', type=str)
    max_upstream = request.args.get('max_upstream', 3, type=int)
    
    results = {}
    
    return jsonify(results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
