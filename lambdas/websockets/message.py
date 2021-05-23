# coding=utf-8

from lambdas.common import RedisManagers
from lambdas.common.ApiResponses import code_200, code_400
from lambdas.common.WebSocketMessage import send as send_web_socket


async def handler(event: dict, *args, **kwargs):
    print(f"received event:\n {event}")
    print("-----")
    print(*args, **kwargs)

    request_ctx = event["requestContext"]

    connection_id = request_ctx["connectionId"]
    domain_name = request_ctx["domainName"]
    stage = request_ctx["stage"]

    try:

        with RedisManagers.VideoQueue() as conn:
            conn.send_a_video(event["body"]["message"])

        await send_web_socket(
            domain_name,
            stage,
            connection_id,
            message="This is a " "reply to your message",
        )
        print("sent message")
    except Exception as e:
        return code_400({"message": "your message could not be received"})
    else:
        return code_200({"message": "disconnected"})
