from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from extensions import db
from models import Exercise
from schemas import ExerciseSchema


exercise_bp = Blueprint("exercises", __name__)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


# =========================
# CREATE EXERCISE
# POST /exercises
# =========================
@exercise_bp.route("/", methods=["POST"])
def create_exercise():
    try:
        data = request.get_json()

        new_exercise = Exercise(
            name=data.get("name"),
            muscle_group=data.get("muscle_group"),
            equipment=data.get("equipment")
        )

        db.session.add(new_exercise)
        db.session.commit()

        return exercise_schema.jsonify(new_exercise), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": "Failed to create exercise"}), 500


# =========================
# GET ALL EXERCISES
# GET /exercises
# =========================
@exercise_bp.route("/", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return exercises_schema.jsonify(exercises), 200


# =========================
# GET SINGLE EXERCISE
# GET /exercises/<id>
# =========================
@exercise_bp.route("/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    return exercise_schema.jsonify(exercise), 200


# =========================
# DELETE EXERCISE
# DELETE /exercises/<id>
# =========================
@exercise_bp.route("/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted successfully"}), 200