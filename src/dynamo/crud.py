from datetime import datetime
from typing import Callable

from boto3.dynamodb.conditions import Attr, Key

from .config import TABLE


def _paginate_all(query: Callable):
    response = query()
    for i in response["Items"]:
        yield i
    while "LastEvaluatedKey" in response:
        response = query(ExclusiveStartKey=response["LastEvaluatedKey"])
        for i in response["Items"]:
            yield i


def get_messages(
    username: str, date_from: datetime, date_to: datetime, **kwargs
) -> list:
    response = TABLE.scan(
        Select="ALL_ATTRIBUTES",
        FilterExpression=Key("username")
        .eq(username)
        .__and__(Key("event").begins_with("MESSAGE"))
        .__and__(
            Attr("metadata.registry_created").gte(int(date_from.timestamp()))
        )
        .__and__(
            Attr("metadata.registry_created").lte(int(date_to.timestamp()))
        ),
        **kwargs,
    )
    return response["Items"]


def get_videos(
    username: str, date_from: datetime, date_to: datetime, **kwargs
) -> list:
    response = TABLE.scan(
        Select="ALL_ATTRIBUTES",
        FilterExpression=Key("username")
        .eq(username)
        .__and__(Key("event").begins_with("PLAY_VIDEO"))
        .__and__(
            Attr("metadata.registry_created").gte(int(date_from.timestamp()))
        )
        .__and__(
            Attr("metadata.registry_created").lte(int(date_to.timestamp()))
        ),
        **kwargs,
        **kwargs,
    )
    return response["Items"]


def get_all_online_users(**kwargs) -> list:
    response = TABLE.scan(
        Select="ALL_ATTRIBUTES",
        FilterExpression=Key("event")
        .eq("CONNECTIONS")
        .__and__(Attr("content").exists())
        ** kwargs,
    )
    return response["Items"]


def get_connections(username, **kwargs) -> list:
    response = TABLE.scan(
        Select="ALL_ATTRIBUTES",
        FilterExpression=Key("event")
        .eq("CONNECTIONS")
        .__and__(Key("username").eq(username))
        .__and__(Attr("content").exists()),
        **kwargs,
    )
    return response["Items"]
