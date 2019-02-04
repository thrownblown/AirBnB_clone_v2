#!/usr/bin/python3
""" flask app web server listening on 0.0.0.0 on port 5000 """
from flask import Flask, render_template, send_from_directory
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ Well Hello There """
    return "Hello HBNB!"


@app.route('/styles/<path:path>')
def static_file(path):
    """ static css path """
    return send_from_directory('static', path)


@app.route("/hbnb")
def hbnb():
    """ Just returns HBNB on a different route """
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """ show the <text> to the user """
    return "C %s" % text.replace("_", " ")


@app.route("/python")
@app.route("/python/<text>")
def py_route(text="is cool"):
    """ show the <text> to the user """
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<int:num>")
def num_route(num):
    """ show the post with the given id, the id is an integer """
    return "%d is a number" % num


@app.route("/number_template/<int:num>")
def template_route(num):
    """ renders template with the given id, the id is an integer """
    return render_template("5-number.html", n=num)


@app.route("/number_odd_or_even/<int:num>")
def odd_route(num):
    """ renders template with the given id and its oddness """
    return render_template("6-number_odd_or_even.html", n=num)


@app.route("/states")
@app.route("/states_list")
def list_states():
    """ returns html of all of the states """
    storage.reload()
    objs = storage.all("State")
    return render_template('7-states_list.html', states=list(objs.values()))


@app.route("/cities_by_states")
def list_cities_by_states():
    """ returns html of all of the states and cities"""
    storage.reload()
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=list(states))


@app.route("/states/<stateid>")
def states_cities(stateid=None):
    """ lists all of the cities by states """
    storage.reload()
    objs = storage.all("State")
    if stateid:
        state = objs["State.{}".format(stateid)]
    else:
        state = None

    return render_template(
        '9-states.html',
        states=list(objs.values()),
        state=state,
        stateid=stateid
    )


@app.route('/hbnb_filters')
def filter_route():
    """ returns html of all of the states, cities and amenities"""
    # import pdb; pdb.set_trace()
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        cities=cities,
        amenities=amenities
    )


@app.teardown_appcontext
def teardown_app(exception):
    """ terminates alchemical session """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
