from src.lambdas.common.ApiResponses import code_200, code_500
from src.lambdas.common.DynamoCrud import WebSocketUsers

MESSAGE_TYPES = ("message", "play_video")


def handler(ctx, event):
    BODY = ctx["body"]

    username = BODY["username"]
    message = BODY["message"]
    try:
        if message_type := BODY["message_type"] not in MESSAGE_TYPES:
            raise ValueError(
                {
                    "error": f"unexpected value [{message_type=}]",
                    "expected_values": str(MESSAGE_TYPES),
                }
            )
        _, item = WebSocketUsers.send_message(
            username=username, message=message, message_type=message_type
        )
    except Exception as e:
        return code_500({"error": str(e)})
    else:
        return code_200(
            {"message": "you successfully send a message!", "created": item}
        )
