#!/usr/bin/python3
"""Script that start Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Shutdown the storage """
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
