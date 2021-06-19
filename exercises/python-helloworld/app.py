from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status_check():
    return jsonify({
            'result': 'OK - healthy'
            })

@app.route("/metrics")
def metrics_check():
    return jsonify({
            'success': True,
            
            })



if __name__ == "__main__":
    app.run(host='0.0.0.0')
