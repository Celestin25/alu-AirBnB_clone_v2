#!/usr/bin/python3
"""Starts a Flask web application that displays a list of states.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: Displays an HTML page with a list of all State objects in the database.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in the database."""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_session(exception=None):
    """Closes the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

