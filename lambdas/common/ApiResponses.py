# coding=utf-8
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
    }


def code_400(data: dict) -> dict:
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 400,
        "body": dumps(data),
    }
