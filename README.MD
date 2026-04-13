# 🏋️ Workout Tracker API

A simple Flask-based backend API for managing workouts and exercises. This project demonstrates a clean relational database design using SQLAlchemy with a many-to-many relationship and additional metadata.

---

## 🚀 Features

* Create and manage workouts
* Create and manage exercises
* Assign exercises to workouts
* Track:

  * Sets
  * Reps
  * Duration
* Data validation at model level
* Database migrations using Flask-Migrate

---

## 🧱 Tech Stack

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite (development)
* Pipenv (environment management)

---

## 📂 Project Structure

```
.
├── app.py
├── models.py
├── extensions.py
├── migrations/
├── Pipfile
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd <project-folder>
```

---

### 2. Install dependencies (Pipenv)

```
pipenv install
```

---

### 3. Activate virtual environment

```
pipenv shell
```

---

### 4. Set environment variable

#### Linux / macOS

```
export FLASK_APP=app.py
```

#### Windows (PowerShell)

```
setx FLASK_APP app.py
```

---

## 🗄️ Database Setup

### Initialize migrations (first time only)

```
flask db init
```

### Generate migration

```
flask db migrate -m "initial migration"
```

### Apply migration

```
flask db upgrade
```

---

## 🧠 Database Models

### Workout

* `id`
* `name` (unique)
* `duration_minutes`
* `created_at`

---

### Exercise

* `id`
* `name` (unique)
* `muscle_group` (legs, arms, core, back, full body)
* `equipment`

---

### WorkoutExercise (Join Table)

* Links workouts and exercises
* Additional fields:

  * `sets`
  * `reps`
  * `duration_seconds`

---

## 🔗 Relationships

* A **Workout** has many **Exercises**
* An **Exercise** can belong to many **Workouts**
* Managed via `WorkoutExercise`

---

## 🧪 Example Usage

### Create a workout

```python
from models import Workout
from extensions import db

workout = Workout(name="Morning Routine", duration_minutes=30)
db.session.add(workout)
db.session.commit()
```

---

### Create an exercise

```python
from models import Exercise

exercise = Exercise(name="Push Ups", muscle_group="arms")
db.session.add(exercise)
db.session.commit()
```

---

### Link exercise to workout

```python
from models import WorkoutExercise

we = WorkoutExercise(
    workout_id=1,
    exercise_id=1,
    sets=3,
    reps=15
)

db.session.add(we)
db.session.commit()
```

---

## ⚠️ Notes

* SQLite is used for development and does not support full transactional DDL.
* Model-level validation ensures:

  * Positive durations
  * Valid muscle groups
  * Minimum name length

---

## 📌 Future Improvements

* REST API endpoints (CRUD)
* User authentication
* Workout history tracking
* Progress analytics
* PostgreSQL support for production


