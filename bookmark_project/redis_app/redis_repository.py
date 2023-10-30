import pickle
import redis
from typing import List
from config import REDIS_HOST, REDIS_PORT

# Создание сессии для работы с БД
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)


class RedisRepository:
    def __init__(self, redis_client: redis.Redis = redis_client):
        self.redis_client = redis_client

    def set_dict(self, key: str, values: dict = None) -> None:
        """
        Динамическое добавление значений в БД. Если поступают спаршенные значения,
        они заносятся в БД, в противном случае создается только одно значение: url
        """
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
        # Кодировка в JSON для добавления данных в БД
        mapping_values = pickle.dumps(mapping_values)
        self.redis_client.set(key, value=mapping_values)
        return

    def get_dict(self, key: str) -> dict | None:
        """Получение значения по ключу key(url)"""
        data = self.redis_client.get(key)
        if data is not None:
            print(data)
            return pickle.loads(data)
        return

    def get_list_dict(self) -> List[dict]:
        """Получение списка всех значений из БД"""
        all_keys = self.redis_client.keys('*')
        data = [self.get_dict(key) for key in all_keys]
        return data
