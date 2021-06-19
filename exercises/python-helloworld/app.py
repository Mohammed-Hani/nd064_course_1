from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status_check():
    return jsonify({
            'success':True,
            'result': 'OK - healthy'
            })

@app.route("/metrics")
def metrics_check():
    metrics_data = {'UserCount': 140, 'UserCountActive': 23}
    return jsonify({
            'success':True,
            'data': metrics_data
            })



if __name__ == "__main__":
    app.run(host='0.0.0.0')
