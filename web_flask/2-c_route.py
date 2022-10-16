#!/usr/bin/python3
"""
Start a Flask Web Application
"""
from flask import Flask
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
def message(text):
    """ Display C with text variable"""
    return 'User {}'.format(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
