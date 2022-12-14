#!/usr/bin/python3
"""
Start a Flask Web Application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display a Message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display a Message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display C with text variable"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Display Python with text variable(text = cool)"""
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display HTML only if n is an integer"""
    return render_template('5-number.html', value=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
