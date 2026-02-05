import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


# ============================
# CUSTOM LEVEL: SUCCESS
# ============================

SUCCESS_LEVEL = 25  # Entre INFO (20) e WARNING (30)

logging.addLevelName(SUCCESS_LEVEL, "SUCCESS")


def success(self, message, *args, **kwargs):
    if self.isEnabledFor(SUCCESS_LEVEL):
        self._log(SUCCESS_LEVEL, message, args, **kwargs)


logging.Logger.success = success


# ============================
# LOGGER SETUP
# ============================

def setup_logger(worker_name="RPA", log_level=logging.INFO):
    """
    Cria logger padrão para RPA workers

    :param worker_name: Nome do worker
    :param log_level: Nível mínimo (INFO, DEBUG, etc)
    """
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
    print(project_root)

    log_dir = f"{project_root}/logs"
    os.makedirs(log_dir, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    log_file = f"{log_dir}/{worker_name}.log"

    logger = logging.getLogger(worker_name)

    # Evita duplicar handlers
    if logger.handlers:
        return logger

    logger.setLevel(log_level)
    logger.propagate = False


    # ============================
    # FORMAT
    # ============================

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%H:%M:%S"
    )


    # ============================
    # FILE HANDLER (ROTATION)
    # ============================

    file_handler = TimedRotatingFileHandler(
        log_file,
        when="midnight",     # gira todo dia
        interval=1,
        backupCount=14,      # mantém 14 dias
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)


    # ============================
    # CONSOLE HANDLER
    # ============================

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)


    # ============================
    # ADD HANDLERS
    # ============================

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger("test")
    logger.success("teste deu certo!!")