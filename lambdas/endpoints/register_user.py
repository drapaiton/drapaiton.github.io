from lambdas.common.ApiResponses import code_200, code_422, code_500
from lambdas.common.DynamoCrud import WebSocketUsers


def handler(ctx, *args, **kwargs):
    new_user: str = ctx["path"]["user"]
    try:
        WebSocketUsers.register_user(username=new_user)
    except ValueError as e:
        return code_422({"error": str(e)})
    except Exception as e:
        return code_500({"error": str(e)})
    else:
        return code_200({"message": f"successfully registered [{new_user}]"})
