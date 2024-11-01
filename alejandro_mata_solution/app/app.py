from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Testing endpoint', 200 

@app.route('/productionplan', methods=['POST'])
def production_plan():
    payload = request.get_json()
    return jsonify(payload), 200