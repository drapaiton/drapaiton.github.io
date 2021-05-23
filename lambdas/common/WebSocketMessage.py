# coding=utf-8
import boto3


def _create(domain_name, stage):
    ENDPOINT = "{domain_name}/{stage}"
    endpoint = ENDPOINT.format(domain_name=domain_name, stage=stage)
    # endpoint_url = 'https://{api-id}.execute-api.{region}.amazonaws.com/{stage}'
    return boto3.client("apigatewaymanagementapi", endpoint_url=endpoint)


def send(domain_name, stage, connection_id, message):
    ws = _create(domain_name, stage)
    return ws.post_to_connection(Data=message, ConnectionId=connection_id)
