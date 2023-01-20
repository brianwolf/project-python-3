
from datetime import datetime
from typing import List
from uuid import uuid4

from logic.apps.example.model import Example
from logic.apps.example import repository
from logic.libs.logger.logger import log


def get_example() -> Example:
    """
    Devuelve un objeto de ejemplo
    """
    example = Example(
        string='string',
        integer=2,
        date_time=datetime.now(),
        double=2.3,
        uuid=uuid4())

    log.info(example)
    return example


def add(m: Example) -> Example:
    """
    Guarda un Example
    """
    m.id = repository.add(m)
    return m


def get_all() -> List[Example]:
    """
    Obtiene todos los Example guardados
    """
    return repository.get_all()
