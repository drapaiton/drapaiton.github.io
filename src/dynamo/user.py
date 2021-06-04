from datetime import datetime
from uuid import uuid4

from boto3.dynamodb.conditions import Attr

from src.common.config import Dynamo

ConditionalCheckFailedException = Dynamo.ConditionalCheckFailedException


class User:
    MESSAGE_TYPES = ("MESSAGE", "PLAY_VIDEO")

    @property
    def is_registered(self):
        response = Dynamo.TABLE.get_item(
            Key={"username": self.username, "event": "REGISTERED"}
        )
        exists = bool(response.get("Item"))
        return exists

    def register_user(self):
        exception = False
        for process in (self._put_connection_set, self._put_registered):
            try:
                process()
            except ValueError as exception:
                continue
        if exception:
            raise ValueError(exception)

    def __init__(self, username: str):
        self.username = username

    def disconnect(self, connection_id: str) -> dict:
        try:
            response = Dynamo.TABLE.update_item(
                Key={"username": self.username, "event": "CONNECTIONS"},
                UpdateExpression="""\
                DELETE content :conn
                SET metadata.updated = :updated""",
                ReturnValues="UPDATED_NEW",
                ExpressionAttributeValues={
                    ":conn": {connection_id},
                    ":updated": int(datetime.now().timestamp()),
                },
                ConditionExpression=Attr("content").contains(connection_id),
            )
        except ConditionalCheckFailedException:
            raise ValueError("connection doesn't exists")
        else:
            return response

    def add_connection(self, connection_id: str) -> dict:
        response = Dynamo.TABLE.update_item(
            Key={"username": self.username, "event": "CONNECTIONS"},
            UpdateExpression="""\
            ADD content :conn
            SET metadata.updated = :updated""",
            ReturnValues="UPDATED_NEW",
            ExpressionAttributeValues={
                ":conn": {connection_id},
                ":updated": int(datetime.now().timestamp()),
            },
        )
        return response

    def send_message(self, message: str, message_type: str):
        if (message_type := message_type.upper()) not in self.MESSAGE_TYPES:
            OUTPUT = {
                "error": f"unexpected value [{message_type=}]",
                "expected_values": str(self.MESSAGE_TYPES),
            }
            raise ValueError(OUTPUT)

        return Dynamo.TABLE.put_item(
            Item={
                "username": self.username,
                "event": f"{message_type} {uuid4()}",
                "content": message,
                "metadata": {
                    "updated": int(datetime.now().timestamp()),
                    "registry_created": int(datetime.now().timestamp()),
                },
            },
            ReturnValues="NONE",
        )

    def _put_connection_set(self):
        try:
            response = Dynamo.TABLE.put_item(
                Item={
                    "username": self.username,
                    "event": "CONNECTIONS",
                    "metadata": {
                        "updated": int(datetime.now().timestamp()),
                        "registry_created": int(datetime.now().timestamp()),
                    },
                },
                ConditionExpression=Attr("event").not_exists(),
                ReturnValues="NONE",
            )
        except ConditionalCheckFailedException:
            raise ValueError("user already exists")
        else:
            return response

    def _put_registered(self):
        try:
            response = Dynamo.TABLE.put_item(
                Item={
                    "username": self.username,
                    "event": "REGISTERED",
                    "metadata": {
                        "updated": int(datetime.now().timestamp()),
                        "registry_created": int(datetime.now().timestamp()),
                    },
                },
                ConditionExpression=Attr("username").not_exists(),
                ReturnValues="NONE",
            )
        except ConditionalCheckFailedException:
            raise ValueError("user already exists")
        else:
            return response

    def __str__(self):
        return str(self.username)

    def __dict__(self):
        return {"username": self.username}
