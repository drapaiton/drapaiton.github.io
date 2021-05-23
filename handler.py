# coding=utf-8
import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "context": {k: str(v) for k, v in context.__dict__.items()},
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
