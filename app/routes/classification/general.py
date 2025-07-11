from flask import jsonify, request
from app.routes.classification import classification_bp
from app.models import Session, GeneralClassification


@classification_bp.route("/general", methods=["GET"])
def get_general():
    session = Session()
    try:
        data = session.query(GeneralClassification).all()
        result = [{"user_id": row.user_id, "time": row.time} for row in data]
        return jsonify(result)
    finally:
        session.close()


@classification_bp.route("/general/<int:user_id>/add", methods=["POST"])
def add_general(user_id):
    session = Session()
    try:
        row = session.query(GeneralClassification).filter_by(user_id=user_id).first()
        if not row:
            return jsonify({"error": f"User {user_id} not found"}), 404

        value = request.json.get("time")
        if value is None or not isinstance(value, int):
            return jsonify({"error": "Missing or invalid 'time' (integer required)"}), 400

        row.time += value
        session.commit()
        return jsonify({"user_id": user_id, "new_time": row.time})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
