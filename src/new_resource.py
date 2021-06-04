from src.common.WebSocketMessage import send
from src.common.responses import (
    AException,
    CreatedResource,
    UnprocessableEntity,
)
from src.dynamo.crud import get_all_online_users
from src.dynamo.user import User


def register_user_handler(event, _):
    print(event)
    new_user: str = event["path"]["user"]
    try:
        user = User(username=new_user)
        user.register_user()
    except ValueError as e:
        return UnprocessableEntity({"error": e}).dict()
    except Exception as e:
        return AException(e).dict()
    else:
        MSG = "you successfully registered a user!"
        return CreatedResource(message=MSG, created=user).dict()


def send_message_handler(event, _):
    print(event)
    body = event["body"]

    user = User(username=body["username"])
    content = body["content"]
    message_type = body["message_type"]
    try:
        created = user.send_message(message=content, message_type=message_type)
        PAYLOAD = {
            "username": user.username,
            "content": content,
            "message_type": message_type,
        }
        print(PAYLOAD)
        send(PAYLOAD, list(get_all_online_users()))
    except ValueError as e:
        return UnprocessableEntity(body=sum([], e.args)[0]).dict()
    except Exception as e:
        return AException(e).dict()
    else:
        MSG = "you successfully send a message!"
        return CreatedResource(message=MSG, created=created).dict()
