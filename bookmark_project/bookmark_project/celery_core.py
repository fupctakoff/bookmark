from celery import Celery
from config import CELERY_BROKER_URL, CELERY_BACKEND_URL

# Создание приложения Селери
app = Celery(
    'bookmark_project',
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL,
    include=['bookmark_project.tasks'])
