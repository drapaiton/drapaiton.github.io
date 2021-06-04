import logging
from os import environ, getenv

import boto3
from boto3 import resource

AWS_REGION = environ["AWS_DEFAULT_REGION"] = "us-east-2"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
TIME_FORMAT = "%H:%M:%S"


if PRODUCTION := bool(getenv("PRODUCTION", 0)):
    CORS_ORIGIN = environ["CORS_ORIGIN"]
    API_GATEWAY_URL = environ["APIG_ENDPOINT"]
    WEB_SOCKET_ENDPOINT = environ["WEB_SOCKET_ENDPOINT"]
else:
    CORS_ORIGIN = getenv("CORS_ORIGIN", "*")
    API_GATEWAY_URL = getenv("APIG_ENDPOINT")
    WEB_SOCKET_ENDPOINT = getenv("WEB_SOCKET_ENDPOINT")


class Dynamo:
    RESOURCE = resource("dynamodb")
    TABLE = RESOURCE.Table("WebSocketUsers")

    ConditionalCheckFailedException = (
        RESOURCE.meta.client.exceptions.ConditionalCheckFailedException
    )


class WebSocket:
    ENDPOINT = WEB_SOCKET_ENDPOINT
    CLIENT = boto3.client(
        "apigatewaymanagementapi",
        endpoint_url=WEB_SOCKET_ENDPOINT,
        region_name=AWS_REGION,
    )

    GoneException = CLIENT.exceptions.GoneException
    LimitExceededException = CLIENT.exceptions.LimitExceededException
