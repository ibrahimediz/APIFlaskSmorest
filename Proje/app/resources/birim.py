import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from .aaa import birimler
from app.schemas import BirimSchema

blp = Blueprint("Birimler", __name__,description="Birimler için operasyonlar")


@blp.route("/birim/<string:birim_id>")
class Birim(MethodView):

    @blp.response(200,BirimSchema)
    def get(self,birim_id):
        try:

            return birimler[birim_id]
        except KeyError:
            abort(404,message="Birim Bulunamadı")

    def delete(self,birim_id):
        try:
            del birimler[birim_id]
            return {"mesaj":"Birim Silindi"}
        except KeyError:
            abort(404, message="Birim Bulunamadı")


@blp.route("/birim")
class BirimList(MethodView):

    @blp.response(200,BirimSchema(many=True))
    def get(self):
        return {"birimler":list(birimler.values())}
    
    @blp.arguments(BirimSchema)
    @blp.response(201,BirimSchema)
    def post(self,birimData):
        for birim in birimler.values():
            if birimData["birim"] == birim["birim"]:
                abort(400,message={"Birim Zaten Oluşturulmuş"})
        birim_ID = uuid.uuid4().hex
        birim = {**birimData,"id":birim_ID}
        birimler[birim_ID] = birim
        return birim

