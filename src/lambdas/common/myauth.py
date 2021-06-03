import logging


def createAuthorizedResponse(resource):
    return {
        "principalId": "me",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": resource,
                }
            ],
        },
    }


def handler(event, context):
    logging.info(event)
    headers = event["headers"]
    methodArn = event["methodArn"]
    return createAuthorizedResponse(methodArn)
