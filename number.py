#!/usr/bin/python3
# from web_flask.hell import app as application
import importlib

odd = importlib.import_module('web_flask.6-number_odd_or_even')


application = odd.app

if __name__ == "__main__":
    application.run()
