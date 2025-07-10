import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'app.db')}"