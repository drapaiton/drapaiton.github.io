from datetime import datetime
from json import dumps
from typing import Union

from pydantic import BaseModel


class ApiResponse(BaseModel):
    headers: dict = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Origin": "*",
    }
    date = str(datetime.now())
    statusCode: int
    body: str


class CreatedResourceResponse(ApiResponse):
    statusCode = 200
    headers: str = dumps(
        {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
        }
    )

    def __init__(self, created: dict, message: str):
        _body = dumps({"created": created, "message": str(message)})
        super().__init__(body=_body)


class ExceptionResponse(ApiResponse):
    statusCode = 500

    def __init__(self, error: Union[str, Exception]):
        super().__init__(body={"message": str(error)})


# noinspection SpellCheckingInspection
class UnprocessableEntityResponse(ApiResponse):
    statusCode = 422

    def __init__(self, body: dict):
        super().__init__(body=body)
