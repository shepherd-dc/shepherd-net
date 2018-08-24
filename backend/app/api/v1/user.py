# from flask import Blueprint
from app.libs.redprint import Redprint

# user = Blueprint('user', __name__)
api = Redprint('user')
@api.route('/get')
def get_user():
    return 'get user'