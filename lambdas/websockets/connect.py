# coding=utf-8
from lambdas.common import RedisManagers
from lambdas.common.ApiResponses import code_200


async def handler(event: dict, *args, **kwargs):
    print(f"received event:\n {event}")
    print("-----")
    print(*args, **kwargs)

    request_ctx = event["requestContext"]

    connection_id = request_ctx["connectionId"]
    domain_name = request_ctx["domainName"]
    stage = request_ctx["stage"]

    with RedisManagers.Connections() as conn:
        conn.add_connection(connection_id, domain_name, stage)

    return code_200({"message": "connected"})
