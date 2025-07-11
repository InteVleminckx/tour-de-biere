from flask import jsonify, request
from app.routes.classification import classification_bp
from app.models import Session, PolkaClassification


@classification_bp.route("/polka", methods=["GET"])
def get_polka():
    session = Session()
    try:
        data = session.query(PolkaClassification).all()
        result = [{"user_id": row.user_id, "points": row.points} for row in data]
        return jsonify(result)
    finally:
        session.close()


@classification_bp.route("/polka/<int:user_id>/add", methods=["POST"])
def add_polka(user_id):
    session = Session()
    try:
        row = session.query(PolkaClassification).filter_by(user_id=user_id).first()
        if not row:
            return jsonify({"error": f"User {user_id} not found"}), 404

        value = request.json.get("points")
        if value is None or not isinstance(value, int):
            return jsonify({"error": "Missing or invalid 'points' (integer required)"}), 400

        row.points += value
        session.commit()
        return jsonify({"user_id": user_id, "new_points": row.points})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
