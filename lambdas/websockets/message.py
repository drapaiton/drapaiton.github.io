# coding=utf-8
from json import loads

from lambdas.common import RedisManagers
from lambdas.common.ApiResponses import code_200, code_400
from lambdas.common.WebSocketMessage import send as send_web_socket


def handler(event: dict, *args, **kwargs):
    request_ctx = event["requestContext"]

    connection_id = request_ctx["connectionId"]
    domain_name = request_ctx["domainName"]
    stage = request_ctx["stage"]

    body = loads(event["body"])
    start_in_seconds = body["start_in_seconds"]
    message = body["message"]
    try:
        conn = RedisManagers.VideoQueue()
        conn.send_a_video(message, start_in_seconds, connection_id)
        conn.close()

        send_web_socket(
            domain_name,
            stage,
            connection_id,
            message="This is a reply to your message",
        )
    except Exception as e:
        print("message could not be send")
        print(e)
        return code_400({"message": "your message could not be received"})
    else:
        print("message send")
        return code_200({"message": "send"})
