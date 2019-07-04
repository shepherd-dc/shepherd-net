# from flask import Blueprint
import json

from flask import jsonify, g, request
from wtforms.validators import email

from app.libs.error_code import DeleteSuccess, Success
from app.libs.redprint import Redprint
from app.libs.restful_json import restful_json
from app.libs.token_auth import auth
from app.models.base import db

from app.models.user import User

# user = Blueprint('user', __name__)
from app.validators.forms import NicknameForm, EmailForm

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/list', methods=['GET'])
@auth.login_required
def super_get_user_list():
    kw = request.args.get('kw', '')
    auth = request.args.get('auth', '')
    status = request.args.get('status', '')
    page_index = int(request.args.get('page', 1))
    page_size = int(request.args.get('limit', 20))

    user = User.query

    if kw:
        user = user.filter(User.nickname.like('%' + kw + '%'))

    if auth:
        user = user.filter_by(auth=auth)

    if status:
        user = user.filter_by(status=status)

    user = user.limit(page_size).offset((page_index - 1) * page_size).all()

    return restful_json(user)


@api.route('/email', methods=['POST'])
def get_email():
    form = EmailForm().validate_for_api()
    email = form.email.data
    user = User.query.filter_by(email=email).first()
    if user:
        data = {
            "error_code": 100,
            "msg": "邮箱已注册"
        }
        return jsonify(data)
    else:
        return Success()


@api.route('/nickname', methods=['POST'])
def get_nickname():
    form = NicknameForm().validate_for_api()
    nickname = form.nickname.data
    user = User.query.filter_by(nickname=nickname).first()
    if user:
        data = {
            "error_code": 101,
            "msg": "昵称已注册"
        }
        return jsonify(data)
    else:
        return Success()


@api.route('/delete', methods=['POST'])
@auth.login_required
def delete_user():
    data = request.get_json('id')
    user = User.query.filter_by(id=data['id']).first_or_404()
    with db.auto_commit():
        user.status = 0
    return DeleteSuccess()


@api.route('/delete', methods=['DELETE'])
@auth.login_required
def super_delete_user():
    data = request.get_json('id')
    user = User.query.filter_by(id=data['id']).first_or_404()
    with db.auto_commit():
        db.session.delete(user)
    return DeleteSuccess()
