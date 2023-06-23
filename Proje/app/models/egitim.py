from app.resources.db import db


class EgitimModel(db.Model):
    __tablename__ = "egitimler"

    id = db.Column(db.Integer,primary_key=True)
    egitim = db.Column(db.String(80),unique=True,nullable=True)
    sure = db.Column(db.Integer,unique=False,nullable=True)
    # birim_id = db.Column(db.Integer,unique=False,nullable=False)

    birim_id = db.Column(db.Integer,db.ForeignKey("birimler.id"),unique=False,nullable=False)
    birim = db.relationship("BirimModel",back_populates="egitimler")
