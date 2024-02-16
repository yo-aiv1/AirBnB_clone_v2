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


@app.route('/c/<text>', strict_slashes=False)
def main2(text):
    """ return the passed string """
    PassedText = text.replace("_", " ")
    return "C {}".format(PassedText)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def main3(text="is cool"):
    """ return the passed string """
    PassedText = text.replace("_", " ")
    return "Python {}".format(PassedText)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
