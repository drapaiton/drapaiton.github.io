# coding=utf-8
from ..common.ApiResponses import code_200
from ..common.config import logger


def handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))

    # request_ctx = event["requestContext"]
    #
    # connection_id = request_ctx["connectionId"]
    # domain_name = request_ctx["domainName"]
    # stage = request_ctx["stage"]
    # conn = get_client()
    # RedisManagers.Connections().add_connection(
    #     connection_id, domain_name, stage, conn
    # )
    # conn.close()
    #
    return code_200({"message": "connected"})
