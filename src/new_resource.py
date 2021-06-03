from .common.WebSocketMessage import send
from .dynamo.crud import get_all_online_users
from .dynamo.user import User
from .common.responses import *
from .common.WebSocketMessage import send


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
        return CreatedResource(message=MSG, created=user).dict()


def send_message_handler(ctx, *args, **kwargs):
    user = User(username=ctx["username"])
    content = ctx["content"]
    message_type = ctx["message_type"]

    try:
        created = user.send_message(message=content, message_type=message_type)
        send(
            {
                "username": user.username,
                "content": content,
                "message_type": message_type,
            },
            get_all_online_users(),
        )
    except ValueError as e:
        return UnprocessableEntity(body=sum([], e.args)[0]).dict()
    except Exception as e:
        return AException(e).dict()
    else:
        MSG = "you successfully send a message!"
        return CreatedResource(message=MSG, created=created).dict()
