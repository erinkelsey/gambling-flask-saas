from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)

SERVER_NAME = config("SERVER_NAME")
