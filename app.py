from flask import Flask, jsonify
from flask_migrate import Migrate

from extensions import db, ma

from controllers.workout_controller import workout_bp
from controllers.exercise_controller import exercise_bp
from controllers.workout_exercise_controller import workout_exercise_bp


def create_app():
    app = Flask(__name__)

    # =========================
    # CONFIGURATION
    # =========================
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workouts.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # =========================
    # INITIALIZE EXTENSIONS
    # =========================
    db.init_app(app)
    ma.init_app(app)

    # 👇 ✅ ADD THIS BLOCK (CRITICAL)
    from models.workout import Workout
    from models.exercise import Exercise
    from models.workout_exercise import WorkoutExercise

    # 👇 Keep this AFTER models are imported
    Migrate(app, db)

    # =========================
    # REGISTER BLUEPRINTS
    # =========================
    app.register_blueprint(workout_bp, url_prefix="/workouts")
    app.register_blueprint(exercise_bp, url_prefix="/exercises")
    app.register_blueprint(workout_exercise_bp)

    # =========================
    # HEALTH CHECK ROUTE
    # =========================
    @app.route("/")
    def home():
        return jsonify({
            "message": "Workout API is running 🚀"
        })

    # =========================
    # GLOBAL ERROR HANDLER
    # =========================
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Route not found"}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": "Internal server error"}), 500

    return app


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)