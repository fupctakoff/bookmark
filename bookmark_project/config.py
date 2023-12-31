import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DJ_SECRET_KEY = os.environ.get('DJ_SECRET_KEY')
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_BACKEND_URL = os.environ.get('CELERY_BACKEND_URL')
