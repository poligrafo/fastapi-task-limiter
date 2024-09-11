# app/core/logging_config.py
import logging
import logging.config
import os


def setup_logging():
    log_directory = '/app/logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": os.path.join(log_directory, "app.log"),
                "formatter": "default",
            },
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
        },
        "loggers": {
            "app": {
                "level": "INFO",
                "handlers": ["file", "console"],
            },
            "uvicorn": {
                "level": "INFO",
                "handlers": ["file", "console"],
                "propagate": False,
            },
            "fastapi": {
                "level": "INFO",
                "handlers": ["file", "console"],
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(LOGGING_CONFIG)
