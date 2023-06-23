import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from .aaa import egitimler
from app.schemas import EgitimSchema,EgitimUpdateSchema

blp = Blueprint("Egitimler",__name__,description="Egitim için operasyonlar")


@blp.route("/egitim/<string:egitim_id>")
class Egitim(MethodView):
    
    @blp.response(200,EgitimSchema)
    def get(self,egitim_id):
        try:
            return egitimler[egitim_id]
        except KeyError:
            abort(404,message="Eğitim Bulunamadı")

    def delete(self,egitim_id):
        try:
            del egitimler[egitim_id]
            return {"mesaj":"Eğitim Silindi"}
        except KeyError:
            abort(404,message="Eğitim Bulunamadı")
    
    @blp.arguments(EgitimUpdateSchema)
    @blp.response(200,EgitimSchema)
    def put(self,egitim_data,egitim_id):
        try:
            egitim = egitimler[egitim_id]
            egitim |= egitimData
            return egitim
        except KeyError:
            abort(404,message="Egitim Bulunamadı")

@blp.route("/egitim")
class EgitimList(MethodView):

    @blp.response(200,EgitimSchema(many=True))
    def get(self):
        return {"egitimler":list(egitimler.values())} 



    @blp.arguments(EgitimSchema)
    @blp.response(201,EgitimSchema)
    def post(self,egitimData):
        for egitim in egitimler.values():
            if (egitimData["egitim"] == egitim["egitim"] and egitimData["sure"] == egitim["sure"]):
                abort(400,message={"Egitim Zaten Oluşturuldu"})
        egitimID = uuid.uuid4().hex
        egitim = {**egitimData,"id":egitimID}
        egitimler[egitimID] = egitim
        return egitim              



