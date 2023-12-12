#!/usr/bin/python3
"""Script that start Flask web app server"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def hello_Ptext(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def hello_num(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
