from extensions import db


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
        allowed = ["legs", "arms", "core", "back", "full body"]

        if len(name.strip()) < 3:
            raise ValueError("Exercise name must be at least 3 characters")

        muscle_group = muscle_group.lower().strip()
        if muscle_group not in allowed:
            raise ValueError(f"muscle_group must be one of {allowed}")

        self.name = name
        self.muscle_group = muscle_group
        self.equipment = equipment

    def __repr__(self):
        return f"<Exercise {self.name}>"