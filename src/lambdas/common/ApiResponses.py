# coding=utf-8
from datetime import datetime
from json import dumps


def code_200(data: dict) -> dict:
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 200,
        "body": dumps(data),
        "date": str(datetime.now()),
    }


def code_422(data: dict) -> dict:
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 422,
        "body": dumps(data),
        "date": str(datetime.now()),
    }


def code_500(data: dict) -> dict:
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 500,
        "body": dumps(data),
        "date": str(datetime.now()),
    }
