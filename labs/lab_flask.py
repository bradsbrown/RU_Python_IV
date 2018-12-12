#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_flask` -- serving up REST
=========================================

LAB_FLASK Learning Objective: Learn to serve RESTful APIs using the Flask library
::

 a. Using Flask create a simple server that serves the following string for the root route ('/'):
  "<h1>Welcome to my server</h1>"

 b. Add a route for "/now" that returns the current date and time in string format.

 c. Add a route that converts Fahrenheit to Centigrade and accepts the value to convert
    in the url.  For instance, /fahrenheit/32.0 should return "0.0"

 d. Add a route that converts Centigrade to Fahrenheit and accepts the value to convert
    in the url.  For instance, /centigrade/0.0 should return "32.0"

"""

import datetime

from flask import Flask
from werkzeug.routing import BaseConverter


class FlexiNumber(BaseConverter):
    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return f"{value:.2f}"

app = Flask(__name__)
app.url_map.converters['number'] = FlexiNumber



@app.route('/')
def root():
    return "<h1>Welcome to my server</h1>"


@app.route("/now")
def get_time():
    return str(datetime.datetime.now())


@app.route("/f/<number:temp>")
@app.route("/fahrenheit/<number:temp>")
def f_to_c(temp):
    return f"{(5 * (temp - 32)) / 9:.2f}"

@app.route("/c/<number:temp>")
@app.route("/celsius/<number:temp>")
def c_to_f(temp):
    return f"{((9 * temp) / 5) + 32:.2f}"

if __name__ == "__main__":
    app.run(debug=True)
