from datetime import datetime
from typing import Union

from pydantic import BaseModel


class ApiResponse(BaseModel):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Origin": "*",
    }
    date = str(datetime.now())
    statusCode: int
    body: dict


class CreatedResourceResponse(ApiResponse):
    statusCode = 200

    def __init__(self, created: dict, message: str):
        super().__init__(body={"created": created, "message": str(message)})


class ExceptionResponse(ApiResponse):
    statusCode = 500

    def __init__(self, error: Union[str, Exception]):
        super().__init__(body={"message": str(error)})


# noinspection SpellCheckingInspection
class UnprocessableEntityResponse(ApiResponse):
    statusCode = 422

    def __init__(self, body: dict):
        super().__init__(body=body)
