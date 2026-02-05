import logging
import os
from datetime import datetime


def setup_logger(worker_name="RPA"):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    log_file = f"{log_dir}/{worker_name}_{today}.log"

    logger = logging.getLogger(worker_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    # Arquivo
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console (Docker / terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
