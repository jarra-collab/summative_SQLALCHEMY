from flask import Blueprint, request, jsonify

from extensions import db
from models import Workout, Exercise, WorkoutExercise
from schemas import WorkoutExerciseSchema


workout_exercise_bp = Blueprint("workout_exercises", __name__)

workout_exercise_schema = WorkoutExerciseSchema()


# ==========================================
# ADD EXERCISE TO WORKOUT
# POST /workouts/<workout_id>/exercises
# ==========================================
@workout_exercise_bp.route("/workouts/<int:workout_id>/exercises", methods=["POST"])
def add_exercise_to_workout(workout_id):
    try:
        data = request.get_json()

        # -------------------------
        # Validate workout exists
        # -------------------------
        workout = Workout.query.get(workout_id)
        if not workout:
            return jsonify({"error": "Workout not found"}), 404

        # -------------------------
        # Validate exercise exists
        # -------------------------
        exercise = Exercise.query.get(data.get("exercise_id"))
        if not exercise:
            return jsonify({"error": "Exercise not found"}), 404

        # -------------------------
        # Prevent duplicate entry (important constraint)
        # -------------------------
        existing = WorkoutExercise.query.filter_by(
            workout_id=workout_id,
            exercise_id=exercise.id
        ).first()

        if existing:
            return jsonify({"error": "Exercise already added to this workout"}), 400

        # -------------------------
        # Create join record
        # -------------------------
        workout_exercise = WorkoutExercise(
            sets=data.get("sets"),
            reps=data.get("reps"),
            duration_seconds=data.get("duration_seconds")
        )

        workout_exercise.workout_id = workout_id
        workout_exercise.exercise_id = exercise.id

        # -------------------------
        # Save to DB
        # -------------------------
        db.session.add(workout_exercise)
        db.session.commit()

        return workout_exercise_schema.jsonify(workout_exercise), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception:
        return jsonify({"error": "Failed to add exercise to workout"}), 500


# ==========================================
# OPTIONAL (Nice for debugging / bonus points)
# GET ALL WORKOUT-EXERCISE LINKS
# GET /workout-exercises
# ==========================================
@workout_exercise_bp.route("/workout-exercises", methods=["GET"])
def get_all_workout_exercises():
    links = WorkoutExercise.query.all()
    return workout_exercise_schema.jsonify(links, many=True), 200