# coding=utf-8
from lambdas.common.ApiResponses import code_200


async def handler(event: dict, *args, **kwargs):
    print(f"received event:\n {event}")
    print("-----")
    print(*args, **kwargs)
    return code_200({"message": "default"})
