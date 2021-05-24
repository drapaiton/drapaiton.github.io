# coding=utf-8
from lambdas.common import RedisManagers
from lambdas.common.ApiResponses import code_200


def handler(event: dict, ctx):
    request_ctx = event["requestContext"]

    connection_id = request_ctx["connectionId"]
    domain_name = request_ctx["domainName"]
    stage = request_ctx["stage"]

    conn = RedisManagers.Connections()
    conn.add_connection(connection_id, domain_name, stage)
    conn.close()

    return code_200({"message": "connected"})
