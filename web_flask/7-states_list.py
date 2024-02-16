#!/usr/bin/python3
""" Flask WebApp """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """ Close """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ Return States """
    states = storage.all(State)
    Data = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=Data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
