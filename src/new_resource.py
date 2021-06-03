from common.DynamoCrud import register_user, send_message
from common.models import (
    CreatedResourceResponse,
    ExceptionResponse,
    UnprocessableEntityResponse,
)


def register_user_handler(ctx, *args, **kwargs):
    new_user: str = ctx["path"]["user"]
    try:
        _, item = register_user(username=new_user)
    except ValueError as e:
        return UnprocessableEntityResponse({"error": e}).dict()
    except Exception as e:
        return ExceptionResponse(e).dict()
    else:
        MSG = "you successfully registered a user!"
        return CreatedResourceResponse(message=MSG, created=item).dict()


MESSAGE_TYPES = (
    "MESSAGE",
    "PLAY_VIDEO",
)


def send_message_handler(ctx, event):
    username = ctx["username"]
    message = ctx["message"]

    if message_type := ctx["message_type"] not in MESSAGE_TYPES:
        ERROR = f"unexpected value [{message_type=}]"
        OUTPUT = {"error": ERROR, "expected_values": str(MESSAGE_TYPES)}
        return UnprocessableEntityResponse(body=OUTPUT).dict()
    try:
        _, item = send_message(
            username=username, message=message, message_type=message_type
        )
    except Exception as e:
        return ExceptionResponse(e).dict()
    else:
        MSG = "you successfully send a message!"
        return CreatedResourceResponse(message=MSG, created=item).dict()
