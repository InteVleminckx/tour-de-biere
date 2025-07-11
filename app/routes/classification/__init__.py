from flask import Blueprint

classification_bp = Blueprint("classification", __name__, url_prefix="/api")

from app.routes.classification import general, points, polka
