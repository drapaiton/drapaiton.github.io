from .dynamo.user import User
from .common.responses import *


def register_user_handler(ctx, *args, **kwargs):
    new_user: str = ctx["path"]["user"]
    try:
        user = User(username=new_user)
    except ValueError as e:
        return UnprocessableEntity({"error": e}).dict()
    except Exception as e:
        return AException(e).dict()
    else:
        MSG = "you successfully registered a user!"
        return CreatedResource(message=MSG, created=user.__dict__()).dict()


MESSAGE_TYPES = (
    "MESSAGE",
    "PLAY_VIDEO",
)


def send_message_handler(ctx, *args, **kwargs):
    user = User(username=ctx["username"])
    message = ctx["message"]
    message_type = ctx["message_type"]

    if message_type not in MESSAGE_TYPES:
        ERROR = f"unexpected value [{message_type=}]"
        OUTPUT = {"error": ERROR, "expected_values": str(MESSAGE_TYPES)}
        return UnprocessableEntity(body=OUTPUT).dict()

    try:
        created = user.send_message(message=message, message_type=message_type)
    except Exception as e:
        return AException(e).dict()
    else:
        MSG = "you successfully send a message!"
        return CreatedResource(message=MSG, created=created).dict()
