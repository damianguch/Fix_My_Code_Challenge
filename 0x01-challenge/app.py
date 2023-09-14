from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status')
def api_status():
    return jsonify({'status': 'API is up and running'})

if __name__ == '__main__':
    app.run(port=4000, debug=True)
