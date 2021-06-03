from datetime import datetime
from typing import Union

from pydantic import BaseModel


class BaseResponse(BaseModel):
    headers: dict = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Origin": "*",
    }
    date = str(datetime.now())
    statusCode: int = 500
    body: dict


class CreatedResource(BaseResponse):
    statusCode = 200

    def __init__(self, created: Union[dict, object], message: str):
        _body = {"created": dict(created), "message": str(message)}
        super().__init__(body=_body)


class AException(BaseResponse):
    statusCode = 500

    def __init__(self, error: Union[str, Exception]):
        super().__init__(body={"message": str(error)})


# noinspection SpellCheckingInspection
class UnprocessableEntity(BaseResponse):
    statusCode = 422

    def __init__(self, body: dict):
        super().__init__(body=body)
