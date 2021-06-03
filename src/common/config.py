import logging
from os import environ, getenv

AWS_REGION = environ["AWS_DEFAULT_REGION"] = "us-east-2"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
TIME_FORMAT = "%H:%M:%S"
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt=TIME_FORMAT,
)


if PRODUCTION := bool(getenv("PRODUCTION", 0)):
    CORS_ORIGIN = environ["CORS_ORIGIN"]
    API_GATEWAY_URL = environ["APIG_ENDPOINT"]
else:
    CORS_ORIGIN = getenv("CORS_ORIGIN", "*")
    API_GATEWAY_URL = getenv("APIG_ENDPOINT")
