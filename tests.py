from os import environ

environ["AWS_DEFAULT_REGION"] = "us-east-2"
environ["AWS_PROFILE"] = "serverlessUser"

from common.DynamoCrud import *
