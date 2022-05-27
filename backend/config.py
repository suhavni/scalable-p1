from os import getenv
from readline import redisplay

class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis
    CACHE_TYPE = 'SimpleCache'
    # CACHE_REDIS_HOST = 'redis'
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_DB = 0
    # CACHE_REDIS_URL = 'redis://redis:6379/0'
    CACHE_DEFAULT_TIMEOUT = 1
