from flask import Flask, jsonify
import logging
from functools import wraps


logging.basicConfig(filename='app.log', format='%(asctime)s, %(message)s', level=logging.INFO)
app = Flask(__name__)

def endpoint_reached(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(func.__name__ + ' endpoint was reached')
        return func(*args, **kwargs)
    return wrapper


@app.route("/")
@endpoint_reached
def hello():
    return "Hello World!"

@app.route("/status")
@endpoint_reached
def status_check():
    return jsonify({
            'success':True,
            'result': 'OK - healthy'
            })

@app.route("/metrics")
@endpoint_reached
def metrics_check():
    metrics_data = {'UserCount': 140, 'UserCountActive': 23}
    return jsonify({
            'success':True,
            'data': metrics_data
            })



if __name__ == "__main__":
    app.run(host='0.0.0.0')
