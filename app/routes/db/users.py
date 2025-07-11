from flask import jsonify, request
from app.routes.db import db_bp
from app.models import Session, Users

@db_bp.route("/users", methods=["GET"])
def get_users():
    session = Session()
    try:
        data = session.query(Users).all()
        result = [{"user_id": row.id, "user_name": row.name} for row in data]
        return jsonify(result)
    finally:
        session.close()
