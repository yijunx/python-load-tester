from flask import Flask
import time


app = Flask(__name__)


@app.route('/slow', methods=["GET"])
def slow():
    time.sleep(1)
    return "slow"


@app.route('/fast', methods=["GET"])
def fast():
    return "fast"



