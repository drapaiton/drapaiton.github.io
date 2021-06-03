from datetime import datetime
from uuid import uuid4
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError

from .config import TABLE
from common.config import logger


class User:
    MESSAGE_TYPES = ("MESSAGE", "PLAY_VIDEO")

    @property
    def is_registered(self):
        response = TABLE.get_item(
            Key={"username": self.username, "event": "REGISTERED"}
        )
        exists = bool(response.get("Item"))
        logger.info(f"{exists=}")
        return exists

    def _register_user(self):
        failed_check = False
        for process in (self._put_connection_set, self._put_registered):
            try:
                process()
            except ValueError as e:
                failed_check = True

        if failed_check:
            raise ValueError(e)

    def __init__(self, username: str):
        self.username = username

        if not self.is_registered:
            self._register_user()

    def disconnect(self, connection_id: str) -> dict:
        try:
            response = TABLE.update_item(
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
        except ClientError as e:
            if (
                e.response["Error"]["Code"]
                == "ConditionalCheckFailedException"
            ):
                logger.exception(e.response["Error"]["Message"])
                raise ValueError("connection doesn't exists")
            else:
                raise
        else:
            return response

    def add_connection(self, connection_id: str) -> dict:
        response = TABLE.update_item(
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
        message_type = message_type.upper()

        if message_type not in self.MESSAGE_TYPES:
            ERROR = f"unexpected value [{message_type=}]"
            OUTPUT = {
                "error": ERROR,
                "expected_values": str(self.MESSAGE_TYPES),
            }
            raise ValueError(OUTPUT)

        return TABLE.put_item(
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
            response = TABLE.put_item(
                Item={
                    "username": self.username,
                    "event": "CONNECTIONS",
                    # "content": set([""]),
                    "metadata": {
                        "updated": int(datetime.now().timestamp()),
                        "registry_created": int(datetime.now().timestamp()),
                    },
                },
                ConditionExpression=Attr("event").not_exists(),
                ReturnValues="NONE",
            )
        except ClientError as e:
            if (
                e.response["Error"]["Code"]
                == "ConditionalCheckFailedException"
            ):
                logger.exception(e.response["Error"]["Message"])
                raise ValueError("user already exists")
            else:
                raise
        else:
            return response

    def _put_registered(self):
        try:
            response = TABLE.put_item(
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
        except ClientError as e:
            if (
                e.response["Error"]["Code"]
                == "ConditionalCheckFailedException"
            ):
                logger.exception(e.response["Error"]["Message"])
                raise ValueError("user already exists")
            else:
                raise
        else:
            return response

    def __str__(self):
        return str(self.username)

    def __dict__(self):
        return {"username": self.username}
