from flask import Flask
from config import Config # ----
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

from .resources.birim import blp as BirimBlueprint
from .resources.egitim import blp as EgitimBlueprint

from .db import db
import app.models

def create_app(db_url=None):
    app = Flask(__name__)
    app.config.from_object(Config) # ---



    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:////data.db")
    db.init_app(app)
    api = Api(app)
    
    with app.app_context():
        db.create_all()

    api.register_blueprint(BirimBlueprint)
    api.register_blueprint(EgitimBlueprint)

    return app

# from app import routes
# from .resources import birimler,egitimler