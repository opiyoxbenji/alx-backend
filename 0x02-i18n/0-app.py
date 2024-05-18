#!/usr/bin/env python3
"""
task 0 - Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def indexing():
    """
    route to hello world
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
