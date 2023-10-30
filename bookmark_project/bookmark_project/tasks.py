from parse.parse_core import ParseResult
from .celery_core import app
from redis_app.redis_repository import RedisRepository


@app.task
def task_get_tags(url: str) -> None:
    """Селери таск для парсинга title, description, favicon"""
    connection = RedisRepository()
    creating_bookmark = ParseResult(url)
    data_for_db = creating_bookmark.get_tags()
    connection.set_dict(url, data_for_db)
    return
