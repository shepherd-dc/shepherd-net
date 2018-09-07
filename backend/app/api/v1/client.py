from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    else:
        raise ClientTypeError()

    return 'client register'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        with db.auto_commit():
            user = User()
            user.nickname = form.nickname.data
            user.email = form.account.data
            user.password = form.secret.data
            db.session.add(user)