#!/usr/bin/python3
""" This module starts a Flask web application """""
from flask import Flask
"""Flask class and render_template method"""
app = Flask(__name__)
app.url_map.strict_slashes = False

""" App route section"""


@app.route('/')
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)