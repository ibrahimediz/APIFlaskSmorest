import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from .db import egitimler
from app.schemas import EgitimSchema,EgitimUpdateSchema
########### DB

from .db import db
from app.models import EgitimModel
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint("Egitimler",__name__,description="Egitim için operasyonlar")


@blp.route("/egitim/<string:egitim_id>")
class Egitim(MethodView):
    
    @blp.response(200,EgitimSchema)
    def get(self,egitim_id):
        egitim = EgitimModel.query.get_or_404(egitim_id)
        return egitim

    def delete(self,egitim_id):
        egitim = EgitimModel.query.get_or_404(egitim_id)
        db.session.delete(egitim)
        db.session.commit()
        return {"message":"Eğitim Silindi"},200
    
    @blp.arguments(EgitimUpdateSchema)
    @blp.response(200,EgitimSchema)
    def put(self,egitim_data,egitim_id):
        item = EgitimModel.query.get(egitim_id)
        if item:
            item.egitim=egitim_data["egitim"]
            item.sure=egitim_data["sure"]
        else:
            item = EgitimModel(id=egitim_id,**egitim_data)
        db.session.add(item)
        db.session.clear()
        return item
  

@blp.route("/egitim")
class EgitimList(MethodView):

    @blp.response(200,EgitimSchema(many=True))
    def get(self):
        return EgitimModel.query.all()



    @blp.arguments(EgitimSchema)
    @blp.response(201,EgitimSchema)
    def post(self,egitimData):
        egitim = EgitimModel(**egitimData)

        try:
            db.session.add(egitim)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="Eğitim Ekleme Sırasında Hata Oluştu")
        return egitim
        # for egitim in egitimler.values():
        #     if (egitimData["egitim"] == egitim["egitim"] and egitimData["sure"] == egitim["sure"]):
        #         abort(400,message={"Egitim Zaten Oluşturuldu"})
        # egitimID = uuid.uuid4().hex
        # egitim = {**egitimData,"id":egitimID}
        # egitimler[egitimID] = egitim
        # return egitim              



