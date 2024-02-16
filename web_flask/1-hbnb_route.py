#!/usr/bin/python3
""" Flask Basic WebApp """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """ return a string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def main1():
    """ return a string """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
