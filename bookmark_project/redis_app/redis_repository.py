import pickle
import redis
from config import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


class RedisRepository:
    def __init__(self, redis_client: redis.Redis = redis_client):
        self.redis_client = redis_client

    def set_dict(self, key: str, values: dict = None) -> None:
        if values:
            mapping_values = {
                "url": key,
                "title": values['title'],
                "description": values['description'],
                "favicon": values['favicon']
            }
        else:
            mapping_values = {
                "url": key
            }
        mapping_values = pickle.dumps(mapping_values)
        data = self.redis_client.set(key, value=mapping_values)
        return

    def get_dict(self, key: str) -> dict:
        data = self.redis_client.get(key)
        return pickle.loads(data)
