from os import environ

environ["AWS_PROFILE"] = "serverlessUser"
from common.config import logger
from dynamo.user import User


if __name__ == "__main__":
    logger.info("debugging")
    user = User("drapaiton")
