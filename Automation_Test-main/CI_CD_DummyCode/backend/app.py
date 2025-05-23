from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from the Python backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
