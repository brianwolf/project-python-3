from logic.apps.admin.config.variables import Vars
from logic.libs.sqliteAlchemy.sqliteAlchemy import Config, setup
from logic.libs.variables.variables import get_var


def setup_sqlite():

    setup(
        Config(
            url=get_var(Vars.DB_SQLITE_PATH),
            echo=bool(get_var(Vars.DB_SQLITE_LOGS)),
            entities_path='logic/apps/*/entity.*'
        )
    )
