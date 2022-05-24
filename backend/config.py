from os import getenv

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    # SECRET_KEY = getenv("SECRET_KEY")
    # FLASK_APP = getenv("FLASK_APP")
    # FLASK_ENV = getenv("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False