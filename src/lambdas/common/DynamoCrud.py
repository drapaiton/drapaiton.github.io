from datetime import datetime
from json import dumps
from typing import Tuple
from uuid import uuid4

import boto3
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError

from .config import logger


RES = boto3.resource("dynamodb")
TABLE = RES.Table("WebSocketUsers")
ConditionalCheckFailedException = (
    RES.meta.client.exceptions.ConditionalCheckFailedException
)


def register_user(username: str) -> Tuple[dict, dict]:
    """if everything is ok, it shall return (response, full item send)"""
    _item = {
        "username": username,
        "event": dumps({"event": "REGISTERED"}),
        "event_date": int(datetime.now().timestamp()),
        "info.id": str(uuid4()),
    }
    try:
        response = TABLE.put_item(
            Item=_item,
            ConditionExpression=Attr("username").not_exists(),
            ReturnValues="NONE",
        )
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            logger.exception(e.response["Error"]["Message"])
            raise ValueError("username already exists")
        else:
            raise
    else:
        return response, _item


def add_connection(username: str, connection_id: str):
    response = TABLE.update_item(
        Key={"username": username, "event": "connections"},
        UpdateExpression="SET info.content = "
        f"list_append(info.content, :id)",
        ReturnValues="UPDATED_NEW",
        ExpressionAttributeValues={
            ":id": [connection_id],
        },
    )
    return response


def send_message(
    username: str,
    message: str,  # message or video
    message_type: str,  # message or video
) -> Tuple[dict, dict]:
    """if everything is ok, it shall return (response, full item send)"""
    _item = {
        "username": username,
        "event": dumps(dict(id=str(uuid4()), event=message_type)),
        "event_date": int(datetime.now().timestamp()),
        "info.content": message,
    }

    response = TABLE.put_item(
        Item=_item,
        ReturnValues="NONE",
    )
    return response, _item
