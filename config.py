import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'O\x88\x11G\x9b\x11\xc2\x88\x9fg\x92Y\xeb)\xae\xd8\xb4W+7\x879K\x81'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = True




