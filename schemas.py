from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.workout import Workout
from models.exercise import Exercise
from models.workout_exercise import WorkoutExercise


# =========================
# EXERCISE SCHEMA
# =========================
class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True


# =========================
# WORKOUT SCHEMA
# =========================
class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True


# =========================
# WORKOUT-EXERCISE SCHEMA
# =========================
class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True