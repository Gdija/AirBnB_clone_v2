#!/usr/bin/python3
"""starting with flask
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!
/hbnb: display "HBNB"
/c/<text>: display c followed by value
/python/<text>: display python followed by value or default
/number/<n>: display n if it is integer
/number_template/<n>:  display a HTML page only if n is an integer
/number_odd_or_even/<n>: check if n even or odd in html temp
"""
from flask import Flask, render_template

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


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_num(n):
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
