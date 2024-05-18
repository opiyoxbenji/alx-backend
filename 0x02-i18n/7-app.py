#!/usr/bin/env python3
"""
Task 7 - Appropriate time zone
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configures HTML classes
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def indexing():
    """
    Route handler for 'Hello World
    """
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """
    Picks the best locale that aligns with the match
    """
    la = request.args.get('locale')
    langua = app.config['LANGUAGES']
    if la in langua:
        return la
    use = request.args.get('login_as')
    if use:
        la = users[int(use)]['locale']
        if la in langua:
            return la
    la = request.headers.get('locale')
    if la in langua:
        return la
    else:
        res = request.accept_languages.best_match(app.config['LANGUAGES'])
        return res


def get_user():
    """
    Fetches all users
    """
    log = request.args.get('login_as')
    if log:
        return users.get(int(log))
    else:
        return None


@app.before_request
def before_request():
    """
    Functions as a decorator
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """
    Determines the timezone
    """
    timez = request.args.get('timezone')
    if timez in pytz.all_timezones:
        return timez
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    use = request.args.get('login_as')
    timez = users[int(use)]['timezome']
    if timez in pytz.all_timezones:
        return timez
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    res = app.config['BABEL_DEFAULT_TIMEZONE']
    return res


if __name__ == '__main__':
    app.run()
