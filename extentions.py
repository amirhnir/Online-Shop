from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()


def get_current_time():
    return round(time.time())