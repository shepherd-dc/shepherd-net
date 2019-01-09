from flask import jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.article import Article
from app.models.base import db
from app.validators.forms import ArticleForm

api = Redprint('article')


@api.route('', methods=['GET'])
def article_list():
    articles = Article.query.all()
    print(articles)
    return jsonify(articles)


@api.route('/<int:aid>', methods=['GET'])
def get_article(aid):
    article = Article.query.filter_by(id=aid).first_or_404()
    return jsonify(article)


@api.route('/publish', methods=['POST'])
def publish_article():
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