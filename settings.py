import os

SECRET_KEY = '\xec\x81\xaaV\xe3\x07s\xdf,\x8d\x83/;OQ\x1f\x11W\x1b\xec\x9d\xa9R\x16'
DEBUG = True

DB_HOST = os.getenv('IP', '0.0.0.0')
DB_USER = 'vishalgupta812'
DB_PASSWORD = ''
DB_NAME = 'blog'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'