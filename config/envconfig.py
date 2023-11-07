import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv('APP_NAME')

RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_PORT = os.getenv('RABBIT_PORT')
RABBIT_QUEUE_NAME = os.getenv('RABBIT_QUEUE_NAME')
RABBIT_USER = os.getenv('RABBIT_USER')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD')

X_RETRIES_LIMIT = os.getenv('X_RETRIES_LIMIT')
DELIVERY_MODE = os.getenv('DELIVERY_MODE')
