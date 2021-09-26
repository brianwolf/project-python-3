from flask import Flask
from logic.libs.reflection import reflection
from logic.libs.rest import rest

api = None

_blueprints_path = 'logic/apps/routes'


def setup_rest(name_flask_app) -> Flask:

    app = Flask(name_flask_app)

    global api
    api = rest.config_flask_app(app)

    reflection.load_modules_by_path(_blueprints_path)

    return app
