from common.config import CORS_ORIGIN, logger
from dynamo.user import User


def handler(event, context):
    logger.info(event)
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
            logger.info(response)
            return response
        else:
            response = {
                "statusCode": 403,
                "headers": {
                    "Content-Type": "text/plain",
                    "Access-Control-Allow-Origin": CORS_ORIGIN,
                },
                "body": "credentials has no access",
            }
            logger.info(response)
            return response
    except Exception as e:
        logger.exception(str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "text/plain",
                "Access-Control-Allow-Origin": CORS_ORIGIN,
            },
            "body": str(e),
        }
