from flask import Flask, request, jsonify
app = Flask(__name__)

students = {}
next_id = 1

@app.route('/')
def home():
    return jsonify({"message": "All good :thumbs_down_emoji"})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)