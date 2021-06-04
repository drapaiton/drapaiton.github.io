from os import environ

AWS_PROFILE = environ["AWS_PROFILE"] = "serverlessUser"
WEB_SOCKET_ENDPOINT = environ["WEB_SOCKET_ENDPOINT"]
AWS_REGION = environ["AWS_DEFAULT_REGION"] = "us-east-2"

import logging
from src.common.WebSocketMessage import send_everyone
from src.common.config import *
from src.dynamo.user import User
from src.dynamo.crud import *
from dateutil.relativedelta import relativedelta


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt=TIME_FORMAT,
    )
    user = User("drapaiton")

    now = datetime.now()
    week_ago = now - relativedelta(days=7)
