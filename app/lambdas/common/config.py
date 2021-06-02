import logging
from os import environ

environ["AWS_DEFAULT_REGION"] = "us-east-2"
logger = logging.getLogger()
logger.setLevel(logging.INFO)
