#!/usr/bin/python3
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)
    app.url_map.strict_slashes = False


    @app.route("/")
    def hello():
        return "Hello HBNB!"
