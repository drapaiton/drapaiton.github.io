# coding=utf-8
from json import dumps
from typing import List

import boto3

from .config import API_GATEWAY_URL, AWS_REGION

WS = boto3.client(
    "apigatewaymanagementapi",
    endpoint_url=API_GATEWAY_URL,
    region_name=AWS_REGION,
)


def send(message: dict, connection_ids: List[str]):
    for _id in connection_ids:
        WS.post_to_connection(Data=dumps(message), ConnectionId=_id)
