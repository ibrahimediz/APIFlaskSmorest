import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from .db import birimler
from app.schemas import BirimSchema
######### DB
from .db import db
from app.models import BirimModel
from sqlalchemy.exc import SQLAlchemyError
############ jwt
from flask_jwt_extended import jwt_required


blp = Blueprint("Birimler", __name__,description="Birimler için operasyonlar")


@blp.route("/birim/<string:birim_id>")
class Birim(MethodView):

    @jwt_required()
    @blp.response(200,BirimSchema)
    def get(self,birim_id):
        birim = BirimModel.query.get_or_404(birim_id)
        return birim

    @jwt_required()
    def delete(self,birim_id):
        birim = BirimModel.query.get_or_404(birim_id)
        try: 
            db.session.delete(birim)
            db.session.commit()
            return {"message":"Birim Silindi"},200
        except SQLAlchemyError as err:
            return {"message":err}
            db.session.rollback()
        finally:
            db.session.close()


@blp.route("/birim")
class BirimList(MethodView):

    @jwt_required()
    @blp.response(200,BirimSchema(many=True))
    def get(self):
        return BirimModel.query.all()
    
    @jwt_required()
    @blp.arguments(BirimSchema)
    @blp.response(201,BirimSchema)
    def post(self,birimData):
        birim = BirimModel(**birimData)
        try:
            db.session.add(birim)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="Birim Ekleme Sırasında Hata Oluştu")
        return birim



