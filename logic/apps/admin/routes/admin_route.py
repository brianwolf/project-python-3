import ntpath
import os

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette.responses import Response

from logic.apps.admin.config.variables import Vars
from logic.libs.logger.logger import log
from logic.libs.variables.variables import all_vars, get_var

apirouter = APIRouter(prefix='', tags=['Admin'])


@apirouter.get('/vars', response_model=dict)
def get_vars():
    return JSONResponse(all_vars())


@apirouter.get('/', response_model=dict)
def alive():
    version = get_var(Vars.VERSION)
    log.info(f'Version: {version}')
    return JSONResponse({'version': version})


@apirouter.get('/postman', response_model=bytes)
def get_postman():

    postman_files = sorted([
        f for f in os.listdir(os.getcwd() + '/logic/resources')
        if str(f).endswith('.postman_collection.json')
    ], reverse=True)

    collection_dir = 'logic/resources/' + next(iter(postman_files), None)
    headers = {
        'Content-Disposition': f'attachment; filename="{ntpath.basename(collection_dir)}"'}

    return Response(
        open(collection_dir, 'rb').read(),
        media_type='application/octet-stream',
        headers=headers
    )
