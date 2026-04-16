from flask import Blueprint, request, jsonify

from extensions import db
from models.workout import Workout
from schemas import WorkoutSchema


workout_bp = Blueprint("workouts", __name__)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)


# =========================
# CREATE WORKOUT
# POST /workouts
# =========================
@workout_bp.route("/", methods=["POST"])
def create_workout():
    try:
        data = request.get_json()

        new_workout = Workout(
            name=data.get("name"),
            duration_minutes=data.get("duration_minutes")
        )

        db.session.add(new_workout)
        db.session.commit()

        return workout_schema.jsonify(new_workout), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception:
        return jsonify({"error": "Failed to create workout"}), 500


# =========================
# GET ALL WORKOUTS
# GET /workouts
# =========================
@workout_bp.route("/", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.jsonify(workouts), 200


# =========================
# GET SINGLE WORKOUT
# GET /workouts/<id>
# =========================
@workout_bp.route("/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    return workout_schema.jsonify(workout), 200


# =========================
# DELETE WORKOUT
# DELETE /workouts/<id>
# =========================
@workout_bp.route("/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted successfully"}), 200