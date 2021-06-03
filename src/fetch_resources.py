from typing import List

from common.config import logger
from dynamo.crud import get_all_online_users


def handler(ctx, *args, **kwargs):
    logger.info(ctx)


def get_connected_users(ctx, *args, **kwargs) -> List:
    return get_all_online_users().get("Item", [])
