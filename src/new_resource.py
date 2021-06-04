from json import dumps

from src.common.WebSocketMessage import send_everyone
from src.common.responses import (
    AException,
    CreatedResource,
    UnprocessableEntity,
)
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
        return CreatedResource(message=MSG, created=str(user)).dict()


def send_message_handler(event, _):
    # TODO refactor the way we send messages
    print(event)
    body = event["body"]

    user = User(username=body["username"])
    message_type = body["message_type"]
    content = dumps(body["content"])
    try:
        # dynamodb
        user.send_message(message=content, message_type=message_type)
        send_everyone(user.username, content, message_type)
    except ValueError as e:
        return UnprocessableEntity(body=sum([], e.args)[0]).dict()
    except Exception as e:
        return AException(e).dict()
    else:
        MSG = "you successfully send a message!"
        created = {
            user.username: "username",
            content: "content",
            message_type: "message_type",
        }
        response = CreatedResource(message=MSG, created=created).dict()

        print(response)
        return response
