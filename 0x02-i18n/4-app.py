#!/usr/bin/env python3
"""
Task 4 - Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    HTML class configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def indexing():
    """
    Route handler for 'Hello World'
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """
    Picks the best locale that aligns with the match
    """
    la = request.args.get('locale')
    langua = app.config['LANGUAGES']
    if la in langua:
        return la
    else:
        res = request.accept_languages.best_match(app.config['LANGUAGES'])
        return res


if __name__ == '__main__':
    app.run()
