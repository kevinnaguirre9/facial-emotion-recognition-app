import os

MONGO_DB_HOST = os.getenv('MONGO_DB_URI', 'mongodb://localhost:27017')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'test')
MONGO_DB_PORT = os.getenv('MONGO_DB_PORT', 27017)
MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME', 'example')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', 'example')
MONGO_DB_URI = os.getenv('MONGO_DB_URI', 'mongodb://localhost:27017')