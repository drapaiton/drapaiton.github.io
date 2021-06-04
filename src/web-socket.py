# coding=utf-8

from src.common.config import logger
from src.common.responses import AException, CreatedResource
from src.dynamo.user import User


def connect_handler(event: dict, _):
    print(event)
    connection_id = event["requestContext"]["connectionId"]
    username = event["queryStringParameters"]["username"]
    try:
        User(username=username).add_connection(connection_id)
    except ValueError as e:
        logger.exception(e)
    return {"statusCode": 200}


def writing_handler(event: dict, _):
    print(event)
    connection_id = event["requestContext"]["connectionId"]
    username = event["queryStringParameters"]["username"]
    User(username=username)
    raise NotImplementedError()


def default_handler(event: dict, _):
    print(event)
    return AException(error="UNKNOWN ERROR 500").dict()


def disconnect_handler(event: dict, _):
    print(event)
    connection_id = event["requestContext"]["connectionId"]
    username = event["queryStringParameters"]["username"]
    try:
        User(username=username).disconnect(connection_id)
    except ValueError as e:
        ...
    return CreatedResource(created={}, message="disconnected").dict()
