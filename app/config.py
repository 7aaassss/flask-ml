import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOAD_FOLDER = os.path.join(basedir, "static")
