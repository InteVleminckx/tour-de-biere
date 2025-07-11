from flask import jsonify, request
from app.routes.db import db_bp
from app.models import Session, Users

def fetch_all_users():
    session = Session()
    try:
        data = session.query(Users).all()
        result = [{"user_id": row.id, "username": row.name} for row in data]
        return result
    finally:
        session.close()


@db_bp.route("/users", methods=["GET"])
def get_users():
   result = fetch_all_users()
   return jsonify(result)