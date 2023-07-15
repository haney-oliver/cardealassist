import json
import logging
import sys
from typing import Any

from fastapi import Request, Response


def get_stream_handler(formatter: logging.Formatter) -> logging.StreamHandler:
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    return stream_handler


def get_logger(name: str, formatter: logging.Formatter) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_stream_handler(formatter))
    return logger


def get_app_log(record) -> dict[str, dict[str, Any]]:
    json_obj = {
        "log": {
            "level": record.levelname,
            "type": "app",
            "timestamp": record.asctime,
            "pathname": record.pathname,
            "line": record.lineno,
            "threadid": record.thread,
            "message": record.message,
        }
    }
    return json_obj


def get_access_log(record) -> dict[str, dict[str, Any]]:
    json_obj = {
        "log": {
            "level": record.levelname,
            "type": "access",
            "timestamp": record.asctime,
            "message": record.message,
        }
    }
    return json_obj


class CustomFormatter(logging.Formatter):
    def __init__(self, formatter: logging.Formatter):
        logging.Formatter.__init__(self, formatter)

    def format(self, record):
        logging.Formatter.format(self, record)
        if not hasattr(record, "extra_info"):
            return json.dumps(get_app_log(record), indent=2)
        else:
            return json.dumps(get_access_log(record), indent=2)


def get_extra_info(request: Request, response: Response) -> dict[str, dict[str, Any]]:
    return {
        "req": {
            "url": request.url.path,
            "headers": request.headers,
            "method": request.method,
            "httpversion": request.scope["http_version"],
            "originalurl": request.url.path,
            "data": request.body,
        },
        "resp": {"status": response.status_code},
    }


app_formatter = CustomFormatter("%(asctime)s")
logger = get_logger(name=__name__, formatter=app_formatter)
