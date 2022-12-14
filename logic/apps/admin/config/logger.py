
from logic.apps.admin.config.variables import Vars
from logic.libs.logger.logger import Config, setup
from logic.libs.variables.variables import get_var


def setup_loggers():
    setup(
        Config(
            path=get_var(Vars.LOGS_PATH),
            level=get_var(Vars.LOGS_LEVEL),
            file_backup_count=int(get_var(Vars.LOGS_BACKUPS))
        )
    )
