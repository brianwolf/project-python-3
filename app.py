#!env/bin/python
import os
import sys

import uvicorn
from fastapi import FastAPI

from logic.apps.admin.config.logger import setup_loggers
from logic.apps.admin.config.rest import setup_rest
from logic.apps.admin.config.sqlite import setup_sqlite
from logic.apps.admin.config.variables import Vars, setup_vars
from logic.libs.variables.variables import get_var

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

app = FastAPI(title='Example API', description='Example python project API')

setup_vars()
setup_loggers()
setup_sqlite()
setup_rest(app)


if __name__ == '__main__':
    uvicorn.run(
        app,
        port=int(get_var(Vars.PYTHON_PORT)),
        host=get_var(Vars.PYTHON_HOST)
    )
