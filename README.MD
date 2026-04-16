# 🏋️ Workout Tracker API

A Flask REST API for managing workouts and exercises using a relational database design with SQLAlchemy. The project follows an **app factory pattern**, uses **Blueprints**, **Flask-Migrate**, and **Marshmallow schemas** for a clean and scalable backend architecture.

---

## 🚀 Features

- Create, read, and delete workouts
- Create, read, and delete exercises
- Assign exercises to workouts (many-to-many relationship)
- Track workout details (sets, reps, duration)
- Model-level validation (rules enforced in Python models)
- RESTful API design using Blueprints
- Database migrations using Flask-Migrate

---

## 🧱 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- SQLite (development)
- Pipenv

---

## 📂 Project Structure
├── app.py
├── config.py
├── extensions.py
├── schemas.py
│
├── models/
│ ├── init.py
│ ├── workout.py
│ ├── exercise.py
│ └── workout_exercise.py
│
├── controllers/
│ ├── workout_controller.py
│ ├── exercise_controller.py
│ └── workout_exercise_controller.py
│
├── migrations/
├── Pipfile
└── README.md


---

## ⚙️ Setup Instructions

### Install dependencies
```bash
pipenv install
pipenv shell
Set Flask app
export FLASK_APP=app:create_app

Windows PowerShell:

$env:FLASK_APP="app:create_app"
🗄️ Database Setup (Flask-Migrate)

Initialize migrations (first time only):

flask db init

Generate migration:

flask db migrate -m "initial migration"

Apply migration:

flask db upgrade

After model changes:

flask db migrate -m "update"
flask db upgrade
    Database Models
Workout
id
name (unique)
duration_minutes
created_at
Exercise
id
name (unique)
muscle_group (legs, arms, core, back, full body)
equipment (optional)
WorkoutExercise (Join Table)
workout_id (FK)
exercise_id (FK)
sets
reps
duration_seconds
🔗 Relationships
A Workout has many Exercises
An Exercise belongs to many Workouts
Managed through WorkoutExercise join table
📡 API Endpoints
Workouts
POST /workouts/
GET /workouts/
GET /workouts/<id>
DELETE /workouts/<id>
Exercises
POST /exercises/
GET /exercises/
GET /exercises/<id>
DELETE /exercises/<id>
Workout Exercises
POST /workout-exercises/
GET /workout-exercises/
DELETE /workout-exercises/<id>
🧪 Example Usage
Create workout
from models.workout import Workout
from extensions import db

workout = Workout(name="Morning Routine", duration_minutes=30)
db.session.add(workout)
db.session.commit()
Create exercise
from models.exercise import Exercise

exercise = Exercise(name="Push Ups", muscle_group="arms")
db.session.add(exercise)
db.session.commit()
Link exercise to workout
from models.workout_exercise import WorkoutExercise

link = WorkoutExercise(
    workout_id=1,
    exercise_id=1,
    sets=3,
    reps=15
)
