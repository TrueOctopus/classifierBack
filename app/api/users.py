# -*- coding: utf-8 -*-
from flask import jsonify, request, flash, render_template, current_app, redirect
from . import api
from ..models import User, db
from datetime import datetime, timedelta


@api.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        accout = request.get_json()
        email = accout.get('email')
        user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({'code': 0, 'message': '用户不存在'})
        else:
            password = accout.get('password')
            if user.verify_password(password):
                json_data = user.to_json()
                json_data['code'] = 1
                json_data['message'] = '登陆成功'
                return jsonify(json_data)
            else:
                return jsonify({'code': -1, 'message': '密码错误'})


@api.route('/users/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        account = request.get_json()
        email = account.get('email')
        password = account.get('password')
        username = account.get('username')

        try:
            user = User(email=email, password=password,
                        username=username)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({'code': 0, 'message': '用户已存在'})
        return jsonify({'code': 1, 'message': '注册成功'})


@api.route('/users/changePassword', methods=['POST', 'GET'])
def changePassword():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({'code': 0, 'message': '用户不存在'})
        else:
            oldPassword = data.get('oldPassword')
            if user.verify_password(oldPassword):
                newPassword = data.get('newPassword')
                user.password = newPassword
                try:
                    db.session.add(user)
                    db.session.commit()
                    return jsonify({'code': 1, 'message': '密码已修改'})
                except Exception as e:
                    return jsonify({'code': -1,
                                    'message': '修改失败：' + str(e)})
            else:
                return jsonify({'code': -2, 'message': '原密码错误'})


def delete(user):
    # noinspection PyBroadException
    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception:
        return False


@api.route('/users/deleteUserById/<int:uid>', methods=['GET'])
def deleteUserById(uid):
    user = User.query.filter_by(id=uid).first()
    if user is None:
        return jsonify({'code': -1, 'message': '用户不存在'})
    if delete(user):
        return jsonify({'code': 1, 'message': '删除成功'})
    else:
        return jsonify({'code': 0, 'message': '删除失败'})


@api.route('/users/changePermission', methods=['POST', 'GET'])
def changePermission():
    if request.method == 'POST':
        uid = request.get_json().get('uid')
        pid = request.get_json().get('pid')
        perm = request.get_json().get('perm')

        user = User.query.filter_by(id=uid).first()
        admin = user.query.filter_by(id=pid).first()

        if not user:
            return jsonify({'code': -1, 'message': '用户不存在'})
        else:
            if admin.permission == 1:
                if admin.id == uid:
                    return jsonify({'code': -5, 'message': '你不能变更自己的权限'})
                user.permission = perm
                try:
                    db.session.add(user)
                    db.session.commit()
                    return jsonify({'code': 1, 'message': '权限变更成功'})
                except Exception as e:
                    print(e)
                    return jsonify({'code': -2, 'message': '添加至数据库失败'})
            else:
                return jsonify({'code': -4, 'message': '权限不足'})
    else:
        return jsonify({'code': -3, 'message': '请求方式错误'})


@api.route('/users/changePersonal', methods=['POST', 'GET'])
def changePersonal():
    if request.method == 'POST':
        uid = request.get_json().get('id')
        username = request.get_json().get('username')
        sex = request.get_json().get('sex')
        phone_num = request.get_json().get('phone_num')
        address = request.get_json().get('address')
        unit = request.get_json().get('unit')

        user = User.query.filter_by(id=uid).first()

        if not user:
            return jsonify({'code': -1, 'message': '用户不存在'})
        else:
            user.username = username
            user.sex = sex
            user.phone_num = phone_num
            user.unit = unit
            user.address = address
            try:
                db.session.add(user)
                db.session.commit()
                return jsonify({'code': 1, 'message': '个人信息修改成功'})
            except Exception as e:
                print(e)
                return jsonify({'code': -2, 'message': '添加至数据库失败'})
    else:
        return jsonify({'code': -3, 'message': '请求方式错误'})


@api.route('/users/addUser', methods=['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        user_data = request.json
        email = user_data.get('email')
        username = user_data.get('username')
        password = user_data.get('password')
        sex = user_data.get('sex')
        phone_num = user_data.get('phone_num')
        address = user_data.get('address')
        unit = user_data.get('unit')
        if all([email, username, password]):
            user = User(email=email, username=username, password=password,
                        sex=sex, phone_num=phone_num, address=address, unit=unit)
        else:
            return jsonify({'code': -1, 'message': '添加失败， 必要信息不全'})
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({'code': 0, 'message': str(e)})
        json_data = user.to_json()
        json_data['code'] = 1
        json_data['message'] = '添加成功'
        return jsonify(json_data)
