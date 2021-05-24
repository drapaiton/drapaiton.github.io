# coding=utf-8
from lambdas.common import RedisManagers
from lambdas.common.ApiResponses import code_200


def handler(event: dict, *args, **kwargs):
    request_ctx = event["requestContext"]
    connection_id = request_ctx["connectionId"]

    conn = RedisManagers.Connections()
    conn.delete_connection(connection_id)
    conn.close()

    return code_200({"message": "disconnected"})
