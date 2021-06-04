import logging
from os import environ

environ["AWS_PROFILE"] = "serverlessUser"
from src.common.config import TIME_FORMAT
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
