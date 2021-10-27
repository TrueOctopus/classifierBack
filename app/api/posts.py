# -*- coding: utf-8 -*-
from flask import jsonify, request, current_app
from ..models import User, db
from . import api
import os


@api.route('/posts/addUser', methods=['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        user_data = request.json
        email = user_data.get('email')
        username = user_data.get('username')
        password = user_data.get('password')
        if all([email, username, password]):
            user = User(email=email, username=username,
                        password=password, confirmed=True)
        else:
            return jsonify({'code': -1, 'message': '添加失败， 信息不全'})
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({'code': 0, 'message': str(e)})
        json_data = user.to_json()
        json_data['code'] = 1
        json_data['message'] = '添加成功'
        return jsonify(json_data)

