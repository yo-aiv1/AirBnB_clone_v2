#!/usr/bin/python3
""" Flask Basic WebApp """
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def main4(n):
    """ return the passed number """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def main5(n):
    """ return the template with passed number """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
