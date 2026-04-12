from datetime import datetime
from extensions import db


# =========================
# WORKOUT MODEL
# =========================
class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    duration_minutes = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to join table
    exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    def __init__(self, name, duration_minutes):
        self.name = name
        self.duration_minutes = duration_minutes

        # simple validation (model-level)
        if len(name.strip()) < 3:
            raise ValueError("Workout name must be at least 3 characters")
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")


# =========================
# EXERCISE MODEL
# =========================
class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    muscle_group = db.Column(db.String(50), nullable=False)
    equipment = db.Column(db.String(120))

    workouts = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    def __init__(self, name, muscle_group, equipment=None):
        self.name = name
        self.muscle_group = muscle_group
        self.equipment = equipment

        allowed = ["legs", "arms", "core", "back", "full body"]
        if len(name.strip()) < 3:
            raise ValueError("Exercise name must be at least 3 characters")
        if muscle_group not in allowed:
            raise ValueError(f"muscle_group must be one of {allowed}")


# =========================
# WORKOUT EXERCISE (JOIN TABLE)
# =========================
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="exercises")
    exercise = db.relationship("Exercise", back_populates="workouts")

    def __init__(self, workout_id, exercise_id, sets=None, reps=None, duration_seconds=None):
        self.workout_id = workout_id
        self.exercise_id = exercise_id

        if sets is not None and sets <= 0:
            raise ValueError("Sets must be greater than 0")
        if reps is not None and reps <= 0:
            raise ValueError("Reps must be greater than 0")
        if duration_seconds is not None and duration_seconds <= 0:
            raise ValueError("Duration must be greater than 0")

        self.sets = sets
        self.reps = reps
        self.duration_seconds = duration_seconds