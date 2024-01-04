#!/usr/bin/python3
"""web flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenities import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(session):
    """remove sqlalchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display content"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
        app.run(host="0.0.0.0")
