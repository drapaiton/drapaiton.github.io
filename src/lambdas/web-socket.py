# coding=utf-8
from common.models import (
    CreatedResourceResponse,
    ExceptionResponse,
)

USERNAME = "drapaiton"


def connect_handler(event: dict, ctx):
    response = CreatedResourceResponse(message="connected", created={}).dict()
    return response
    # return {"statusCode": 200, "body": "connected!", "headers": ""}


def default_handler(event: dict, ctx):
    print(event)
    return ExceptionResponse(error="UNKNOWN ERROR 500").dict()


def disconnect_handler(event: dict, ctx):
    print(event)
    return CreatedResourceResponse(created={}, message="disconnected").dict()


def writing_handler(event: dict, ctx):
    raise NotImplementedError()
