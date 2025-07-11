from flask import Blueprint

db_bp = Blueprint("db", __name__, url_prefix="/api")

from app.routes.db import users
