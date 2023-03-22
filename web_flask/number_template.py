#!/usr/bin/python3
"""Flask web application that listens on 0.0.0.0, port 5000.
Routes:
    /: Returns 'Hello HBNB!'.
    /hbnb: Returns 'HBNB'.
    /c/<text>: Returns 'C' followed by <text>.
    /python/(<text>): Returns 'Python' followed by <text>.
    /number/<n>: Returns '<n> is a number' only if <n> is an integer.
    /number_template/<n>: Returns an HTML page only if <n> is an integer.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns 'C' followed by <text>.
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns 'Python' followed by <text>.
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns '<n> is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns an HTML page only if <n> is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

