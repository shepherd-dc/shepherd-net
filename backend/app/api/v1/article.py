import time

from flask import jsonify, request

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.article import Article
from app.models.base import db
from app.models.menu import Menu
from app.models.submenu import Submenu
from app.validators.forms import ArticleForm

api = Redprint('article')


@api.route('', methods=['GET'])
def article_list():
    menu_id = request.values.get('menu_id', '')
    column_id = request.values.get('column_id', '')
    if menu_id and not column_id:
        menu = Menu.query.filter_by(id=menu_id).first_or_404()
        if menu:
            articles = Article.query.filter_by(menu_id=menu_id).order_by(Article.create_time.desc()).all()
            return jsonify(articles)

    if column_id:
        submenu = Submenu.query.filter_by(id=column_id).first_or_404()
        if submenu:
            articles = Article.query.filter_by(column_id=column_id).order_by(Article.create_time.desc()).all()
            return jsonify(articles)

    articles = Article.query.order_by(Article.create_time.desc()).all()
    return jsonify(articles)


@api.route('/<int:aid>', methods=['GET'])
def get_article(aid):
    article = Article.query.filter_by(id=aid).first_or_404()
    return jsonify(article)


@api.route('/publish', methods=['POST'])
def publish_article():
    form = ArticleForm().validate_for_api()

    title = form.title.data
    article_title = Article.query.filter_by(title=title).first()

    column_id = form.column_id.data
    column = Submenu.query.filter_by(id=column_id).first()

    if article_title:
        data = {
            "error_code": 100,
            "msg": "文章标题重复"
        }
        return jsonify(data)
    else:
        with db.auto_commit():
            article = Article()
            article.title = form.title.data
            article.author = form.author.data
            article.content = form.content.data
            article.column_id = form.column_id.data
            article.column_name = column.name
            article.menu_id = column.menu_id
            article.en_name = column.menu.en_name
            article.menu_name = column.menu.menu_name
            article.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            db.session.add(article)
        return Success()


@api.route('/edit', methods=['POST'])
def edit_article():
    form = ArticleForm().validate_for_api()
    title = form.title.data
    article = Article.query.filter_by(title=title).first()
    if article:
        data = {
            "error_code": 100,
            "msg": "文章标题重复"
        }
        return jsonify(data)
    else:
        with db.auto_commit():
            article = Article()
            article.title = form.title.data
            article.author = form.author.data
            article.content = form.content.data
            article.column_id = form.column_id.data
            db.session.add(article)
        return Success()


@api.route('/<int:aid>', methods=['DELETE'])
@auth.login_required
def delete_article(aid):
    with db.auto_commit():
        article = Article.query.filter_by(id=aid).first_or_404()
        article.delete()
    return DeleteSuccess()


@api.route('/<int:aid>', methods=['DELETE'])
@auth.login_required
def super_delete_article(aid):
    with db.auto_commit():
        article = Article.query.filter_by(id=aid).first_or_404()
        article.delete()
    return DeleteSuccess()