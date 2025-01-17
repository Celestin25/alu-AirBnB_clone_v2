#!/usr/bin/python3
"""
This script starts a Flask web application that listens on 0.0.0.0, port 5000.
The following routes are defined:
- /: displays 'Hello HBNB!'
- /hbnb: displays 'HBNB'
- /c/<text>: displays 'C' followed by the value of <text>
- /python/(<text>): displays 'Python' followed by the value of <text>
- /number/<n>: displays 'n is a number' only if <n> is an integer
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays 'C' followed by the value of <text>, with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """Displays 'Python' followed by the value of <text>, with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Displays '<n> is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

