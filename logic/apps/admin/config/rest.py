
from fastapi import FastAPI

from logic.libs.rest.rest import setup


def setup_rest(app: FastAPI):

    setup(app, 'logic/apps/admin/routes')
    setup(app, 'logic/apps/*/route.*')
