from flask import Flask
from config import Config # ----
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
import os

from .resources.birim import blp as BirimBlueprint
from .resources.egitim import blp as EgitimBlueprint
from .resources.user import blp as UserBlueprint

from .resources.db import db
import app.models

from flask_jwt_extended import JWTManager
from flask import jsonify

def create_app(db_url=None):
    app = Flask(__name__)
    app.config.from_object(Config) # ---



    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    db.init_app(app)
    api = Api(app)
    
    jwt = JWTManager(app)  

    @jwt.expired_token_loader
    def gec_jeton_tekrar_cagir(jwt_header,jwt_payload):
        return (jsonify({"message":"Token süresi geçti","error":"token_expired"}),401)  

    with app.app_context():
        db.create_all()

    api.register_blueprint(BirimBlueprint)
    api.register_blueprint(EgitimBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

app = create_app()
# from app import routes
# from .resources import birimler,egitimler