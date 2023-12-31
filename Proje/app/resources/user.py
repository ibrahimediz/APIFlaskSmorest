from flask.views import MethodView
from flask_smorest import Blueprint,abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

from .db import db
from app.models import UserModel
from app.schemas import UserSchema

blp = Blueprint("Users","users",description="Kullanıcı İşlemleri")

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"],user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token":access_token},200
        abort(401,message="Geçersiz Bilgi")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409,message="Sunucu Taraflı Sorun")
        user = UserModel(username=user_data["username"],password=pbkdf2_sha256.hash(user_data["password"]))
        db.session.add(user)
        db.session.commit()
        return {"message":"Kullanıcı Oluşturuldu"},201

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200,UserSchema)
    def get(self,user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self,user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"Kullanıcı Silindi"},200

