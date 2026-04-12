from app import create_app
from extensions import db
from models import Workout, Exercise, WorkoutExercise

app = create_app()


def seed_database():
    with app.app_context():

        print("Dropping and recreating database...")

        # =========================
        # RESET DATABASE
        # =========================
        db.drop_all()
        db.create_all()

        # =========================
        # EXERCISES
        # =========================
        squat = Exercise(
            name="Squat",
            muscle_group="legs",
            equipment="barbell"
        )

        push_up = Exercise(
            name="Push Up",
            muscle_group="arms",
            equipment=None
        )

        plank = Exercise(
            name="Plank",
            muscle_group="core",
            equipment=None
        )

        db.session.add_all([squat, push_up, plank])
        db.session.commit()

        # =========================
        # WORKOUTS
        # =========================
        leg_day = Workout(
            name="Leg Day",
            duration_minutes=60
        )

        full_body = Workout(
            name="Full Body Blast",
            duration_minutes=45
        )

        db.session.add_all([leg_day, full_body])
        db.session.commit()

        # =========================
        # WORKOUT EXERCISES (JOIN TABLE)
        # =========================
        link1 = WorkoutExercise(
            workout_id=leg_day.id,
            exercise_id=squat.id,
            sets=4,
            reps=10,
            duration_seconds=None
        )

        link2 = WorkoutExercise(
            workout_id=full_body.id,
            exercise_id=push_up.id,
            sets=3,
            reps=15,
            duration_seconds=None
        )

        link3 = WorkoutExercise(
            workout_id=full_body.id,
            exercise_id=plank.id,
            sets=None,
            reps=None,
            duration_seconds=60
        )

        db.session.add_all([link1, link2, link3])
        db.session.commit()

        print("Database seeded successfully! 🚀")


# =========================
# RUN SEED SCRIPT
# =========================
if __name__ == "__main__":
    seed_database()