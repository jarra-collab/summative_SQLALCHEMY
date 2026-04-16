from extensions import db


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    __table_args__ = (
        db.UniqueConstraint("workout_id", "exercise_id", name="unique_workout_exercise"),
    )

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False,
        index=True
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False,
        index=True
    )

    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="exercises")
    exercise = db.relationship("Exercise", back_populates="workouts")

    def __init__(self, workout_id, exercise_id, sets=None, reps=None, duration_seconds=None):
        if sets is not None and sets <= 0:
            raise ValueError("Sets must be greater than 0")

        if reps is not None and reps <= 0:
            raise ValueError("Reps must be greater than 0")

        if duration_seconds is not None and duration_seconds <= 0:
            raise ValueError("Duration must be greater than 0")

        if reps is None and duration_seconds is None:
            raise ValueError("Either reps or duration_seconds must be provided")

        self.workout_id = workout_id
        self.exercise_id = exercise_id
        self.sets = sets
        self.reps = reps
        self.duration_seconds = duration_seconds

    def __repr__(self):
        return f"<WorkoutExercise workout={self.workout_id} exercise={self.exercise_id}>"