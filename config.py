"""
Add your custom configurations to config_local.py
Configurations on config_local.py overwrite the configurations in this file.
"""


class BaseConfig:
    RESTPLUS_MASK_SWAGGER = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    SECRET_KEY = 'kwikkerSecretKeyIsSALTS'
    CODE_KEY = 'kwikkerCode'
    ERROR_404_HELP = False
    DATABASE_NAME = 'kwikker'
    DATABASE_USERNAME = 'postgres'
    DATABASE_PASSWORD = ''
    DATABASE_HOST = None
    DATABASE_PORT = 5432
    MIGRATIONS_DATABASE_NAME = 'migrations'
    SERVER_PATH = 'http://127.0.0.1:5000/'
    MAIL_SERVER = 'smtp.zoho.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'no-reply@kwikker.me'
    MAIL_PASSWORD = 'Kwikker1!'
    FRONT_END_ROOT = 'http://www.kwikker.me'


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    DATABASE_USERNAME = 'kwikker'
    DATABASE_PASSWORD = '8Av5R7tRNqJSm4sXW23E'
    DATABASE_HOST = 'ec2-3-122-42-152.eu-central-1.compute.amazonaws.com'
    SERVER_PATH = 'http://kwikkerbackend.eu-central-1.elasticbeanstalk.com/'


class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_NAME = 'kwikker_test'
    MIGRATIONS_DATABASE_NAME = 'migrations_test'


class ProductionTestingConfig(ProductionConfig):
    TESTING = True
    DATABASE_NAME = 'kwikker_test'
    MIGRATIONS_DATABASE_NAME = 'migrations_test'
