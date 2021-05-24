# coding=utf-8
from lambdas.common.ApiResponses import code_200


def handler(event: dict, ctx):
    return code_200({"message": "default"})
