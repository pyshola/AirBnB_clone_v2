#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/airbnb-onepage_2', strict_slashes=False)
def airbnb_onepage():
    """DIsplays 'Hello HBHB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
