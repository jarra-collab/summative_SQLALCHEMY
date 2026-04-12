from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validates, ValidationError
from models import Workout, Exercise, WorkoutExercise


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise


class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout


class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise