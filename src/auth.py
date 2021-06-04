from src.common.config import CORS_ORIGIN
from src.dynamo.user import User


def generate_policy(event):
    try:
        username = event["queryStringParameters"]["username"]
        if User(username).is_registered:
            response = {
                "principalId": "username",
                "policyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "execute-api:Invoke",
                            "Effect": "Allow",
                            "Resource": "*",
                        }
                    ],
                },
            }
            return response
        else:
            response = {
                "principalId": "username",
                "policyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "execute-api:Invoke",
                            "Effect": "Deny",
                            "Resource": "*",
                        }
                    ],
                },
            }
            return response
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "text/plain",
                "Access-Control-Allow-Origin": CORS_ORIGIN,
            },
            "body": str(e),
        }


def handler(event, _):
    print(event)
    output = generate_policy(event)
    print(output)
    return output
