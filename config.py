import os

class Config(object):
  SECRET_KEY=os.environ.get('SECRET_KEY') or "okay for dev, but set real key for prod"
