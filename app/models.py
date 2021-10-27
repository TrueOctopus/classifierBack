# -*- coding: utf-8 -*-
from flask import current_app
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)  # id
    username = db.Column(db.String(64), unique=True)  # 昵称
    sex = db.Column(db.Integer)  # 性别 important
    phone_num = db.Column(db.String(11), unique=True)  # 电话 important
    email = db.Column(db.String(64), unique=True, index=True)  # 邮箱地址
    password_hash = db.Column(db.String(128))  # 密码
    address = db.Column(db.String(128))  # 地址
    unit = db.Column(db.String(128))  # 地址
    permission = db.Column(db.Integer)  # 用户权限

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.permission is None:
            if self.email == current_app.config['FLASK_ADMIN']:
                self.permission = 1
            if self.permission is None:
                self.permission = 0

    @property
    def password(self):
        raise AttributeError('密码未设定')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def forgetPwdConfirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('pwd') != self.id:
            return False
        return True

    def to_json(self):
        json_user = {
            'id': self.id,
            'username': self.username,
            'sex': self.sex,
            'phone_num': self.phone_num,
            'email': self.email,
            'address': self.address,
            'unit': self.unit
        }
        return json_user

    def __repr__(self):
        return '<User %r>' % self.username
