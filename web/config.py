import os

class BaseConfig(object):
    EMAIL_ADDRESS = "contact@techoffgrid.com"
    EMAIL_PASSWORD = "ryggveien"
    SECRET_KEY = os.urandom(32)
    MAIL_SERVER = 'send.one.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = EMAIL_ADDRESS
    MAIL_PASSWORD = EMAIL_PASSWORD
    MAIL_DEFAULT_SENDER = EMAIL_ADDRESS
    MAIL_MAX_EMAILS = 5
    MAIL_ASCII_ATTACHMENTS = False

    # SECRET_KEY = os.environ['SECRET_KEY']
    # DEBUG = os.environ['DEBUG']
    # DB_NAME = os.environ['DB_NAME']
    # DB_USER = os.environ['DB_USER']
    # DB_PASS = os.environ['DB_PASS']
    # DB_SERVICE = os.environ['DB_SERVICE']
    # DB_PORT = os.environ['DB_PORT']
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    #     DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    # )

# class BaseConfig(object):
#     SECRET_KEY = 'hi'
#     DEBUG = True
#     DB_NAME = 'postgres'
#     DB_SERVICE = 'localhost'
#     DB_PORT = 5432
#     SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}/{2}'.format(
#         DB_SERVICE, DB_PORT, DB_NAME
#     )
