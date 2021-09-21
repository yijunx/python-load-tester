from flask import Flask
import requests


app = Flask(__name__)


RESOURCE_URL = "http://resource_app:8000"


def bad_fibo(n: int) -> int:
    # to keep cpu busy
    if n < 2:
        return n
    else:
        return bad_fibo(n - 1) + bad_fibo(n - 2)


@app.route("/get_slow_resource", methods=["GET"])
def slow():
    return requests.get(f"{RESOURCE_URL}/slow").content


@app.route("/get_fast_resource", methods=["GET"])
def fast():
    return requests.get(f"{RESOURCE_URL}/fast").content


@app.route("/cpu_bound_resource", methods=["GET"])
def stuck():
    return str(bad_fibo(32))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
