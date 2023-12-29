#!/usr/bin/python3
"""starting with flask
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """function to return hello on 0.0.0.0:5000"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
