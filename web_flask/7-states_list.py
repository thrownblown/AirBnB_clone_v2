#!/usr/bin/python3
""" flask app web server listening on 0.0.0.0 on port 5000 """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ Well Hello There """
    return "Hello HBNB!"


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


@app.route("/states_list")
def list_states():
    """ returns html of all of the states """
    storage.reload()
    objs = storage.all("State")
    return render_template('7-states_list.html', states=list(objs.values()))


@app.teardown_appcontext
def teardown_app(exception):
    """ terminates alchemical session """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
