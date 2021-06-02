# coding=utf-8
from ..common.ApiResponses import code_200
from ..common.config import logger


def handler(event: dict, ctx):
    logger.info(str(ctx) + str(event))
    return code_200({"message": "default"})
