# coding=utf-8
from common.DynamoCrud import update_user
from common.config import logger
from common.models import (
    CreatedResourceResponse,
    ExceptionResponse,
)


def connect_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))
    USERNAME = "drapaiton"
    response = update_user(username=USERNAME, connected=True)

    return CreatedResourceResponse(message="connected", created=response)


def default_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))
    return ExceptionResponse(error="UNKNOWN ERROR 500")


def disconnect_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))
    USERNAME = "drapaiton"
    response = update_user(username=USERNAME, connected=False)
    return CreatedResourceResponse(created=response, message="disconnected")


def writing_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))
    raise NotImplementedError()
