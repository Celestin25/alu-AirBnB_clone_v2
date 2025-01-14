#!/usr/bin/python3

"""
A Flask web application that listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"

@app.route("/c/<string:text>", strict_slashes=False)
def c_route(text):
    """Displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_route(text):
    """Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

