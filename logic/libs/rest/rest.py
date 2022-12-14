"""
Rest
----
1.0.0

Dependencias:
* logger
* exception
* reflection

Configura el app de FastAPI para cargar blueprints dinamicamente, agregar JSON decoders que sigan un estandar, 
agregar handlers para manejo automatico de errores, entre otros.
"""
from fastapi import FastAPI

from logic.libs.reflection import reflection
from logic.libs.rest.src.decorators import add_decorators
from logic.libs.rest.src.json import config_encoders


def setup(app, path) -> FastAPI:
    '''
    Configura la app de FastAPI
    '''
    # app.config.setdefault('ERROR_INCLUDE_MESSAGE', False)
    add_decorators(app)
    config_encoders(app)

    load_routes_by_regex_path(app, path)

    return app


def load_routes_by_regex_path(app: FastAPI, path: str):
    '''
    Carga los blueprints al app de FastAPI
    '''
    for module in reflection.load_modules_by_regex_path(path):
        if hasattr(module, 'apirouter'):
            app.include_router(module.apirouter)
