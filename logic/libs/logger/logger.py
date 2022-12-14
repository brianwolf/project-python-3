"""
Logger
-------
1.1.0

Crea logs de la aplicacion
"""
import logging
from dataclasses import dataclass

import logic.libs.logger.src.config as config
from logic.libs.logger.src.file import make_logger


@dataclass
class Config():
    """
    Objeto de configuracion
    """
    path: str = '/tmp/logs/app.log'
    level: str = 'INFO'
    file_backup_count: int = 3


def setup(con: Config):
    """
    Configura las opciones PREDEFINIDAS del logger para el proyecto, en caso del handler, 
    el que viene rota los logs con un archivo por dia hasta hasta un maximo de 7 archivos.
    """
    config._LOGGER = make_logger(con)


def logger() -> logging.Logger:
    """
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea.\n
    En caso de pasarle un fileHandler el path del mismo debe existir 
    """
    return config._LOGGER
