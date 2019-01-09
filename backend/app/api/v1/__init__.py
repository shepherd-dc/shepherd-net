from flask import Blueprint
from app.api.v1 import user, book, client, token, gift, menu, article


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    # user.api.register(bp_v1, url_prefix = '/user')
    # if url_prefix is None: url_prefix = '/' + Redprint().name
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    book.api.register(bp_v1)
    token.api.register(bp_v1)
    gift.api.register(bp_v1)
    menu.api.register(bp_v1)
    article.api.register(bp_v1)

    return bp_v1
