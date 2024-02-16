#!/usr/bin/python3
""" Flask WebApp """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """ Close """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_html(id=None):
    """ Return states and citits """
    states = storage.all(State)

    if not id:
        dict_to_html = {value.id: value.name for value in states.values()}
        return render_template('7-states_list.html',
                               Table="States",
                               items=dict_to_html)

    data = "State.{}".format(id)
    if data in states:
        return render_template('9-states.html',
                               Table="State: {}".format(states[k].name),
                               items=states[k])

    return render_template('9-states.html',
                           items=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
