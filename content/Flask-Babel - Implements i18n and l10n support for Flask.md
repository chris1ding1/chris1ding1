---
title: Flask-Babel - Implements i18n and l10n support for Flask
keywords:
  - Python
  - i18n
  - date formatting
  - timezones
  - Flask
  - translate
  - l10n
  - Flask-Babel
created: 2025-02-20 13:30:58
updated: 2025-01-20 13:30:58
---

Flask-Babel is an extension to Flask that adds i18n and l10n support to any Flask application with the help of babel, pytz and its own copy of speaklater. It has built-in support for date formatting including timezones, as well as a very simple and friendly interface to gettext translations.

[Flask-Babel documentation](https://python-babel.github.io/flask-babel/)

## Directory Structure

```tree
/flask-project
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── templates/
│   │   ├── base.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_db.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

## Installation

```console
pip install Flask-Babel
```

## `__init__.py`

```python
from flask import Flask
from flask_babel import Babel

def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['de', 'fr', 'en'])

def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

app = Flask(__name__, instance_relative_config=True)

""""
https://python-babel.github.io/flask-babel/#configuration
config.py: 
BABEL_DEFAULT_LOCALE: This defaults to 'en'.
BABEL_DEFAULT_TIMEZONE: This defaults to 'UTC' which also is the timezone your application must use internally.
...
""""
app.config.from_pyfile('config.py')

babel = Babel(app, [locale_selector=get_locale, timezone_selector=get_timezone])
```

## Translating Applications

create a mapping file. `touch babel.cfg`

`vim babel.cfg`

```cfg
[python: **.py]
[jinja2: **/templates/**.html]
```

Then it’s time to run the pybabel command that comes with Babel to extract your strings.

```console
pybabel extract -F babel.cfg -o messages.pot .
```

This will use the mapping from the babel.cfg file and store the generated template in messages.pot.

For example to translate to Chinese (Simplified) use this command:

```console
pybabel init -i messages.pot -d flaskr/translations -l zh_Hans_CN
```

Directory structure of the generated translation files:

```tree
/flask-project
├── flaskr/
    ├── translations/
        └── zh_Hans_CN/
            └── LC_MESSAGES/
                └── messages.po
```

Defining translation content: `vim flaskr/translations/zh_Hans_CN/LC_MESSAGES/messages.po`.

```po
msgid "Hello"
msgstr "您好"
```

To compile the translations for use.

```console
pybabel compile -d translations
```

Template files

```html
{{_("Hello")}}
```

Show: "您好"
