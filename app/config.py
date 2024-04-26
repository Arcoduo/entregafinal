import os

class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "++rXyzMeGq4EnI4r0mMBahC6TnBoyI0RjfBacJJ/")

    # Database configuration
    # Update with your RDS endpoint and database credentials
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://andres:12345678@cfflaskappentrega3-flaskdbinstance-uovviynrqluk.cp8ea8umy28n.eu-north-1.rds.amazonaws.com/andresdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # S3 Bucket configuration
    # Add your S3 Bucket for static files
    S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "andres-flask-app-static-381492082403-eu-north-1")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configurations

# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
