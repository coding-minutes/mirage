import os


class Config:
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_HOST = os.environ.get("POSTGRES_HOST")
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASS = os.environ.get("POSTGRES_PASSWORD")

    DEFAULT_CODE_LENGTH = int(os.environ.get("DEFAULT_CODE_LENGTH", '6'))
