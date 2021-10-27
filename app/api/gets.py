# -*- coding: utf-8 -*-
from flask import Response, jsonify, request, current_app
from sqlalchemy import text

from . import api
from ..models import User


@api.route('/gets/getById/<int:uid>', methods=['GET'])
def getById(uid):
    user = User.query.filter_by(id=uid).first()
    if not user:
        return jsonify({'msg': '用户不存在'}), 200
    return jsonify(user.to_json()), 201


@api.route('/gets/getByEmail/<email>', methods=['GET'])
def getByEmail(email):
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'msg': '用户不存在'}), 200
    return jsonify(user.to_json()), 201


@api.route('/gets/getList', methods=['GET', 'POSt'])
def getList():
    pageNum = request.get_json().get('pageNum')
    pageSize = request.get_json().get('pageSize')
    username = request.get_json().get('username')
    sex = request.get_json().get('sex')
    email = request.get_json().get('email')
    phone_num = request.get_json().get('phone_num')
    uid = request.get_json().get('uid')
    user = User.query.filter_by(id=uid).first()
    permission = user.permission
    if permission == 1:
        all_results = User.query.filter(
            User.username.like(
                "%" + username + "%") if username is not None else text(''),
            User.sex.like(
                "%" + sex + "%") if sex is not None else text(''),
            User.email.like(
                "%" + email + "%") if email is not None else text(''),
            User.phone_num.like(
                "%" + phone_num + "%") if phone_num is not None else text('')
        )
        count = len(all_results.all())
        json_data = []
        page = all_results.paginate(page=pageNum,
                                    per_page=pageSize)
        for i in page.items:
            json_data.append(i.to_json())
        data = {'data': json_data, 'count': count}
        return jsonify(data), 201
