from typing import Callable

from boto3.dynamodb.conditions import Key

from . import TABLE


def get_users(username: str, **kwargs):
    response = TABLE.scan(
        Select="ALL_ATTRIBUTES",
        FilterExpression=Key("username")
        .eq(username)
        .__and__(Key("event").begins_with("MESSAGE")),
        ConditionalOperator="AND",
        **kwargs,
    )
    return response


def paginate_all(query: Callable):
    response = query()
    for i in response["Items"]:
        yield i
    while "LastEvaluatedKey" in response:
        response = query(ExclusiveStartKey=response["LastEvaluatedKey"])
        for i in response["Items"]:
            yield i
