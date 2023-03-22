# Import Flask and render_template from Flask
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Define routes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'

@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """Display 'C' followed by the value of <text>"""
    return f'C {text.replace("_", " ")}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python(text='is cool'):
    """Display 'Python' followed by the value of <text>"""
    return f'Python {text.replace("_", " ")}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display '<n> is a number' if <n> is an integer"""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if <n> is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page only if <n> is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0')

