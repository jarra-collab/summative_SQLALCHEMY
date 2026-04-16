from datetime import datetime
from extensions import db


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    duration_minutes = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    def __init__(self, name, duration_minutes):
        if len(name.strip()) < 3:
            raise ValueError("Workout name must be at least 3 characters")
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")

        self.name = name
        self.duration_minutes = duration_minutes

    def __repr__(self):
        return f"<Workout {self.name}>"