from .common import *

DEBUG = False

AWS_ACCESS_KEY_ID = "××××××××××××××××××××"
AWS_SECRET_ACCESS_KEY = "××××××××××××××××××××××××××××××××××××××××"
AWS_STORAGE_BUCKET_NAME = "recipe-post2"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL
