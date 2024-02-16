#!/usr/bin/python3
""" Flask Basic WebApp """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """ return a string """
    return "Hello HBNB!"


app.run(port=5000)
