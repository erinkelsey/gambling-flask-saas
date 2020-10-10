from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)

SERVER_NAME = config("SERVER_NAME")

SECRET_KEY = config("SECRET_KEY")
