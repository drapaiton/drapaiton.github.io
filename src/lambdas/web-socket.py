# coding=utf-8
from .common.ApiResponses import code_200
from .common.config import logger


def connect_handler(event: dict, ctx):
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


def default_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))
    return code_200({"message": "default"})


def disconnect_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))

    # request_ctx = event["requestContext"]
    # connection_id = request_ctx["connectionId"]
    #
    # conn = get_client()
    # RedisManagers.Connections().delete_connection(connection_id, conn)
    # conn.close()

    return code_200({"message": "disconnected"})


def writing_handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))

    # request_ctx = event["requestContext"]
    # connection_id = request_ctx["connectionId"]
    #
    # conn = get_client()
    # RedisManagers.Connections().delete_connection(connection_id, conn)
    # conn.close()

    return code_200({"message": "writing"})
