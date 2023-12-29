#!/usr/bin/python3
"""starting with flask
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!
/hbnb: display "HBNB"
/c/<text>: display c followed by value"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """function to return hello on 0.0.0.0:5000"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    return f'C {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
