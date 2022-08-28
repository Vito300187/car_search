import redis
import time


class RedisConnect:
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)

    def redis_set(self, value):
        self.redis.set(value, time.time_ns())

    def redis_get(self, value):
        return self.redis.get(value)

    def get_all_keys(self):
        return [i for i in self.redis.scan_iter()]

    def remove_all_keys(self):
        self.redis.delete(*self.get_all_keys())
