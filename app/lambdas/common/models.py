from datetime import datetime

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
        super().__init__(body={"created": created, "message": message})


class ExceptionResponse(ApiResponse):
    statusCode = 500

    def __init__(self, error: str):
        super().__init__(body={"message": error})


# noinspection SpellCheckingInspection
class UnprocessableEntityResponse(ApiResponse):
    statusCode = 422

    def __init__(self, error: str):
        super().__init__(body={"message": error})
