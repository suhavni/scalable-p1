from os import getenv
from readline import redisplay

class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis
    CACHE_TYPE = 'FileSystemCache'
    CACHE_DIR = 'cache'
    CACHE_THRESHOLD = 1
    # CACHE_REDIS_HOST = 'redis'
    # CACHE_REDIS_PORT = 'redis'
    # CACHE_REDIS_DB = 0
    # CACHE_REDIS_URL = 'redis://redis:6379/0'
    CACHE_DEFAULT_TIMEOUT = 1
