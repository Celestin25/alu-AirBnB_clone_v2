#!/usr/bin/python3
"""
Creates a Flask web application that listens on 0.0.0.0, port 5000.
The application has one route, which displays 'Hello HBNB!' when accessed.
"""

from flask import Flask

# Create an instance of the Flask class
application = Flask(__name__)

# Define the route for the application
@application.route("/", strict_slashes=False)
def display_hello_hbnb():
    """
    Displays 'Hello HBNB!' when the '/' route is accessed.
    """
    return "Hello HBNB!"

# Run the application
if __name__ == "__main__":
    application.run(host="0.0.0.0")

