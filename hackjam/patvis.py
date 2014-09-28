from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax/graph/', methods=['GET'])
def ajax_graph():
    pat_id = request.args.get('pat_id', type=int)
    max_upstream = request.args.get('max_upstream', 3, type=int)
    results = {}
    
    return jsonify(results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
