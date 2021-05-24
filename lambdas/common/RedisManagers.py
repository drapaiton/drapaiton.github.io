# coding=utf-8
import re
from datetime import datetime
from os import environ
from json import dumps
from typing import List

import redis

REDIS_HOST: str = environ["REDIS_HOST"]
REDIS_PASS: str = environ["REDIS_PASS"]
REDIS_PORT: int = int(environ["REDIS_PORT"])


class RedisRWModel:
    client: redis.Redis

    def close(self):
        self.client.close()

    def __del__(self, *args, **kwargs):
        self.client.close()


class VideoQueue(RedisRWModel):
    QUEUE_NAME = "VideoQueue"
    QUEUE_MAXIMUM_SIZE = 50
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS)

    def send_a_video(
        self, video_id: str, start_in_seconds: int, connection_id: str
    ):
        saved_date: float = datetime.now().timestamp()
        PAYLOAD = {
            "video_id": video_id,
            "start_in_seconds": start_in_seconds,
            "saved_date": saved_date,
            "duration": 600,
            "connection_id": connection_id,
        }
        # keep history short
        self.client.ltrim("VideoQueue", 0, self.QUEUE_MAXIMUM_SIZE)
        self.client.lpush(self.QUEUE_NAME, dumps(PAYLOAD))

    def get_queued_videos(self):
        return self.client.lrange(self.QUEUE_NAME, 0, self.QUEUE_MAXIMUM_SIZE)


class Connections(RedisRWModel):
    LIST_NAME = "Connections"
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS)
    QUEUE_MAXIMUM_SIZE = 50

    def add_connection(self, connection_id: str, domain_name: str, stage: str):
        # keep history short
        PAYLOAD = {
            "connection_id": connection_id,
            "date": datetime.now().timestamp(),
            "domainName": domain_name,
            "stage": stage,
        }
        self.client.ltrim("VideoQueue", 0, self.QUEUE_MAXIMUM_SIZE)
        self.client.lpush(self.LIST_NAME, dumps(PAYLOAD))

    def delete_connection(self, connection_id):
        lon = self.client.llen(self.LIST_NAME)
        CHUNK_SIZE = 10
        for page in range(0, lon + 1, CHUNK_SIZE):
            page_objects: List[bytes] = self.client.lrange(
                self.LIST_NAME, page, page + CHUNK_SIZE
            )
            r = re.compile(connection_id)
            for coincidence in filter(r.search, map(str, page_objects)):
                REMOVE_ALL = 0
                self.client.lrem(self.LIST_NAME, REMOVE_ALL, coincidence)

    def get_all_connection_id(self):
        return self.client.lrange(self.LIST_NAME, 0, self.QUEUE_MAXIMUM_SIZE)
