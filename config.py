import os


class Config:
    """
    Base configuration class (shared settings)
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key (needed for sessions, security, etc.)
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")


class DevelopmentConfig(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///workouts.db"
    )


class ProductionConfig(Config):
    """
    Production environment configuration
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(Config):
    """
    Testing environment configuration
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"