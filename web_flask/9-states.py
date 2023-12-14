#!/usr/bin/python3
"""Script that start Flask web app"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Render html page of state list"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """Render html page of state with given id and its city list"""
    states = storage.all(State)

    state_found = None
    for state in states.values():
        if state.id == id:
            state_found = state
            break
    if state_found:
        return render_template("9-states.html", state_found=state_found)
    else:
        return render_template("9-states.html", state_found=None)


@app.teardown_appcontext
def remove_session(exception):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
