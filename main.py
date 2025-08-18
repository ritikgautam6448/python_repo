from flask import Flask, request, jsonify   

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return "home"

    if __name__ == '__main__':
        app.run(debug=True) 