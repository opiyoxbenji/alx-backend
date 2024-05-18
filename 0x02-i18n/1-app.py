#!/usr/bin/env python3
"""
script for task 0
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    conbfiguratio nclass for html
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def indexing():
    """
    index route and func
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
