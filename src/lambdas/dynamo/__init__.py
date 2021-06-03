from boto3 import resource

RES = resource("dynamodb")
TABLE = RES.Table("WebSocketUsers")
ConditionalCheckFailedException = (
    RES.meta.client.exceptions.ConditionalCheckFailedException
)
