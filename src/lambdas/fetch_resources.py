from src.lambdas.common.config import logger


def handler(ctx, event):
    logger.info(str(ctx) + str(event))
