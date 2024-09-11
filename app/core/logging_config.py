import logging
import logging.config
import os

def setup_logging():
    log_dir = "/app/logs"
    os.makedirs(log_dir, exist_ok=True)

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": f"{log_dir}/app.log",
            },
        },
        "loggers": {
            "app": {  # Логгер для "app"
                "level": "INFO",
                "handlers": ["console", "file"],
                "propagate": False,
            },
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["console", "file"],
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(logging_config)
