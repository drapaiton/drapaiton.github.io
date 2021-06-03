# coding=utf-8

from common.config import logger
from common.responses import AException, CreatedResource
from dynamo.user import User


def connect_handler(event: dict, *args, **kwargs):
    logger.info(event)
    username = event["queryStringParameters"]["username"]
    User(username=username)
    return {"statusCode": 200}


def writing_handler(event: dict, *args, **kwargs):
    raise NotImplementedError()


def default_handler(event: dict, *args, **kwargs):
    logger.info(event)
    return AException(error="UNKNOWN ERROR 500").dict()


def disconnect_handler(event: dict, *args, **kwargs):
    logger.info(event)

    return CreatedResource(created={}, message="disconnected").dict()
