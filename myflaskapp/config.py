
import os


class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-only-secret")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
