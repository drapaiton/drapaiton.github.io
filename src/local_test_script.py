import logging
from os import environ

environ["AWS_PROFILE"] = "serverlessUser"
from common.config import TIME_FORMAT
from dynamo.user import User


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=logging.DEBUG,
        datefmt=TIME_FORMAT,
    )
    user = User("drapaiton")
