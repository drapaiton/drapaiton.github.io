# coding=utf-8
from functools import partial
from json import dumps
from typing import List

from .config import WebSocket
from ..dynamo.crud import get_all_online_users


def send_everyone(
    username: str,
    message: str,
    message_type: str,
    connection_ids: List[str] = list(get_all_online_users()),
):
    PAYLOAD = {
        "username": username,
        "content": message,
        "message_type": message_type,
    }

    reply = partial(WebSocket.CLIENT.post_to_connection, Data=dumps(PAYLOAD))

    for _id in connection_ids:
        try:
            reply(ConnectionId=_id)
        except WebSocket.GoneException:
            continue
        except WebSocket.LimitExceededException:
            continue
