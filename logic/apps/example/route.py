from typing import Dict

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from logic.apps.example import dto, service
from logic.apps.example.error import ExampleError
from logic.libs.exception.exception import AppException

apirouter = APIRouter(prefix='/api/v1/examples')


@apirouter.get('/')
def get():
    result = service.get_example()
    return dto.example_to_json(result)


@apirouter.post('/')
def post(json_data: Dict[str, object]):
    m = dto.json_to_example(json_data)
    m = service.add(m)
    return JSONResponse(dto.example_to_json(m), 201)


@apirouter.get('/all')
def get_all():
    result = service.get_all()
    return JSONResponse([dto.example_to_json(o) for o in result], 200)


@ apirouter.get('/errors/unknow')
def error_unknow():
    boom = 1 / 0
    return JSONResponse('', 200)


@ apirouter.get('/errors/business')
def error_business():
    try:
        1 / 0

    except Exception as e:
        raise AppException(
            code=ExampleError.EXAMPLE_RANDOM_ERROR,
            msj='BOOM...!!!',
            exception=e
        )

    return JSONResponse('', 200)
