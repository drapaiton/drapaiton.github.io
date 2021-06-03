# coding=utf-8
from datetime import datetime
from json import dumps

from common.responses import (
    CreatedResource,
    AException,
)
from dynamo.user import User


def connect_handler(event: dict, ctx):

    User()
    return {
        "statusCode": 200,
    }


def default_handler(event: dict, ctx):
    print(event)
    return ExceptionResponse(error="UNKNOWN ERROR 500").dict()


def disconnect_handler(event: dict, ctx):
    print(event)
    return CreatedResourceResponse(created={}, message="disconnected").dict()


def writing_handler(event: dict, ctx):
    raise NotImplementedError()
