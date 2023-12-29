#!/usr/bin/python3
"""starting with flask"""
from flask import Flask

app = Flask(__name__)
"""name of the application's module"""

@app.route("/", strict_slashes=False)
def hello_route():
    """function to return hello on 0.0.0.0:5000"""
    return "Hello HBNB!"
if __name__ == "__main__":
    app.run(host="0.0.0.0")

