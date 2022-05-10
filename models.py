""""
models -
Author：wiki
Date：2022/5/6
"""
from exts import db
from datetime import datetime
from flask_login import UserMixin,LoginManager

class AdminModel(db.Model):
    __tablename__ = 'admin'
    AdminId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AdminEmail = db.Column(db.String(100), nullable=False, unique=True)
    AdminName = db.Column(db.String(200), nullable=False, unique=True)
    # AdminNick = db.Column(db.String(200), nullable=False)
    AdminPassword = db.Column(db.String(200), nullable=False)
    AdminSex = db.Column(db.Boolean)
    AdminJoin_time = db.Column(db.DateTime, default=datetime.now)


class UserModel(db.Model,UserMixin):
    __tablename__ = 'user'
    UserId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserEmail = db.Column(db.String(100), nullable=False, unique=True)
    UserName = db.Column(db.String(200), nullable=False, unique=True)
    UserIdcard = db.Column(db.String(18), unique=True)
    UserSex = db.Column(db.Boolean)
    UserAddress = db.Column(db.String(200))
    UserPhone = db.Column(db.String(20))
    UserPassword = db.Column(db.String(200), nullable=False)
    UserCredit = db.Column(db.Integer)
    UserJoin_time = db.Column(db.DateTime, default=datetime.now)


class EvaluationModel(db.Model):
    __tablename__ = 'evaluation'
    EvaluationId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EvaluationDescribe = db.Column(db.String(1024), nullable=False)
    EvaluationPicture = db.Column(db.BLOB)
    EvaluationScore = db.Column(db.Integer)
    EvaluationTime = db.Column(db.DateTime, default=datetime.now)
    UserId = db.Column(db.Integer), db.ForeignKey('user.UserId', ondelete='RESTRICT')
    OrderId = db.Column(db.Integer, db.ForeignKey('order.OrderId', ondelete='RESTRICT'))


class GoodsModel(db.Model):
    __tablename__ = 'goods'
    GoodsId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    GoodsPrice = db.Column(db.Float, nullable=False)
    GoodsStock = db.Column(db.Integer, nullable=False)
    GoodsDescribe = db.Column(db.String(1024), nullable=False)
    GoodsTime = db.Column(db.DateTime, default=datetime.now)
    UserId = db.Column(db.Integer, db.ForeignKey('user.UserId', ondelete='RESTRICT'))


class OrderModel(db.Model):
    __tablename__ = 'order'
    OrderId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderExpress = db.Column(db.String(200), unique=True)
    OrderNum = db.Column(db.Integer, nullable=False)
    OrderAddress = db.Column(db.String(200), nullable=False)
    OrderPhone = db.Column(db.String(11), nullable=False)
    OrderTime = db.Column(db.DateTime, default=datetime.now)
    OrderIsfinished = db.Column(db.Boolean)
    UserId = db.Column(db.Integer, db.ForeignKey('user.UserId', ondelete='RESTRICT'))
    GoodsId = db.Column(db.Integer, db.ForeignKey('goods.GoodsId', ondelete='RESTRICT'))


class CommentModel(db.Model):
    __tablename__ = 'comment'
    CommentId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CommentDescribe = db.Column(db.String(1024), nullable=False)
    CommentTime = db.Column(db.DateTime, default=datetime.now)
    UserId = db.Column(db.Integer, db.ForeignKey('user.UserId', ondelete='RESTRICT'))
    GoodsId = db.Column(db.Integer, db.ForeignKey('goods.GoodsId', ondelete='RESTRICT'))
    CommentReply = db.Column(db.Integer, db.ForeignKey('comment.CommentId', ondelete='RESTRICT'))


class ReturnModel(db.Model):
    __tablename__ = 'return'
    ReturnId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ReturnAddress = db.Column(db.String(200), nullable=False)
    ReturnReason = db.Column(db.String(200), nullable=False)
    ReturnTime = db.Column(db.DateTime, default=datetime.now)
    ReturnExpress = db.Column(db.String(200), unique=True)
    ReturnIsfinished = db.Column(db.Boolean)
    UserId = db.Column(db.Integer, db.ForeignKey('user.UserId', ondelete='RESTRICT'))
    OrderId = db.Column(db.Integer, db.ForeignKey('order.OrderId', ondelete='RESTRICT'))

class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)