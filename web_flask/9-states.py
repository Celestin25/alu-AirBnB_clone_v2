#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    state = storage.get("State", id)
    if state:
        return render_template("9-states.html", states=[state])
    return render_template("9-states.html")


@app.teardown_appcontext
def close_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

