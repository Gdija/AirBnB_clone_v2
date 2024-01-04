#!/usr/bin/python3
"""web flask """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(session):
    """remove sqlalchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def list_cities():
    """ list cities of state"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
