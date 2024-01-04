#!/usr/bin/python3
"""web flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(session):
    """remove sqlalchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def list_states():
    """ list state"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id():
    """list states by id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
