from app.db import db

class BirimModel(db.Model):
    __tablename__ = "birimler"

    id = db.Column(db.Integer,primary_key=True)
    birim = db.Column(db.String(80),unique=True,nullable=True)

    egitimler = db.relationship("EgitimModel",back_populates="birim",lazy="dynamic")