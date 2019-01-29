#!/usr/bin/python3
""" flask app web server listening on 0.0.0.0 on port 5000 """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello():
    """ Well Hello There """
    return "Hello HBNB!"


app.run("0.0.0.0")
