from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/employees', methods=['GET', 'POST'])
def get_employees():
    url = 'http://localhost:3001/employees'
    if request.method == 'GET':
        response = requests.get(url)
        # print(response.json())
        return jsonify(response.json())
    if request.method == 'POST':
        data = request.json
        response = requests.post(url, json=data)
        return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)