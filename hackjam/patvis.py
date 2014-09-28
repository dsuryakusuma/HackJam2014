from flask import Flask, render_template, request, jsonify
from keyword_search import key_word_search_result as keyword_search
import random

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
    max_height_above = request.args.get('max_height_above', 3, type=int)
    results = build_referenced_pat_graph(pat_id, max_height_above)
    return jsonify(results=results)

def build_referenced_pat_graph(pat_id, depth):
    if depth <= 0:
        return None
    referenced_pat_ids = [random.randint(1000000, 9999999) for i in range(random.randint(3, 10))];
    out = {}
    for referenced_pat_id in referenced_pat_ids:
        referenced_pats = build_referenced_pat_graph(referenced_pat_id, depth - 1)
        out[referenced_pat_id] = {
            'title': 'Method for appropriating great riches with minimal exertion',
            'references': referenced_pats}
    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
