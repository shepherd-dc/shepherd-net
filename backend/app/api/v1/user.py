# from flask import Blueprint
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

# user = Blueprint('user', __name__)
api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    return 'get user'
