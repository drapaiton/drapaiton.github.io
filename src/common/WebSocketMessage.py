# coding=utf-8
from typing import List

import boto3

from .config import AWS_REGION


def _create(domain_name: str, stage: str):
    ENDPOINT = "https://{domain_name}/{stage}"
    endpoint = ENDPOINT.format(domain_name=domain_name, stage=stage)
    return boto3.client(
        "apigatewaymanagementapi",
        endpoint_url=endpoint,
        region_name=AWS_REGION,
    )


def send(
    domain_name: str, stage: str, connection_ids: List[str], message: str
):
    ws = _create(domain_name, stage)
    for _id in connection_ids:
        ws.post_to_connection(Data=message, ConnectionId=_id)
