from redis_app.redis_repository import RedisRepository
import requests

# Постоянная переменная для запроса в requests
HEADER = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36 '}


class ValidatorUrl:
    @classmethod
    def request_validation(cls, url: str) -> None | bool:
        """Валидация url с помощью запроса по данному url"""
        try:
            response = requests.get(url, headers=HEADER)
        except requests.exceptions.ConnectionError:
            return None
        return True

    @classmethod
    def db_validation(cls, key: str) -> None | bool:
        """Валидация key(url) на существование в БД"""
        connection = RedisRepository()
        if connection.get_dict(key):
            return None
        return True
