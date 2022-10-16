"""
    Script to start a Flask Web Application
"""
from flask import Flask

app=Flask(__name__)

app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a message"""
    return 'Hello HBNB!'

if __name__=='__main__':
    app.run(debug=True)