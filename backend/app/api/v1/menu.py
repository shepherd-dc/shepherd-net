import time

from flask import jsonify, request
from sqlalchemy import inspect, and_

from app.libs.error_code import Success, ParameterException
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.menu import Menu
from app.models.submenu import Submenu
from app.validators.forms import MenuForm, SubmenuForm

api = Redprint('menu')


@api.route('')
def get_menu():
    nav = request.values.get('nav', '')
    menus = Menu.query.all()

    if nav=='nav':
        for menu in menus:
            for submenu in menu.submenu:
                submenu.hide('pic')

    elif nav and nav != 'nav':
        return ParameterException()

    return jsonify(menus)

@api.route('/submenu')
def get_submenu():
    page_index = int(request.args.get('page', 1))
    page_size = int(request.args.get('limit', 20))
    menu_id = request.args.get('menu_id', '')
    name = request.args.get('name', '')

    submenus = Submenu.query

    if name:
        submenus = Submenu.query.filter(Submenu.name.like('%' + name + '%'))
        # submenus = Submenu.query.filter(Submenu.name.like('%'+name+'%')).limit(page_size).offset((page_index-1)*page_size).all()

    if menu_id:
        submenus = submenus.filter(Submenu.menu_id == menu_id)
        # submenus = Submenu.query.filter(and_(Submenu.menu_id == menu_id, Submenu.name.like('%' + name + '%'))).limit(page_size).offset(
        #     (page_index - 1) * page_size).all()

    total = submenus.count()
    submenus = submenus.limit(page_size).offset((page_index - 1) * page_size).all()
    data = {
        "total": total,
        "data": submenus
    }

    return jsonify(data)

@api.route('/list/<en_name>')
def get_list(en_name):
    list = Menu.query.filter_by(en_name=en_name).first_or_404()
    return jsonify(list)

@api.route('/sublist/<name>')
def get_sublist(name):
    sublist =Submenu.query.filter_by(name=name).first_or_404()
    return jsonify(sublist)

@api.route('/add/menu', methods=['POST'])
def add_menu():
    form = MenuForm().validate_for_api()
    with db.auto_commit():
        menu = Menu()
        menu.menu_name = form.menu_name.data
        menu.en_name = form.en_name.data
        menu.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        db.session.add(menu)
    return Success()

@api.route('/add/submenu', methods=['POST'])
def add_submenu():
    form = SubmenuForm().validate_for_api()
    menu = Menu.query.filter_by(id=form.menu_id.data).first_or_404()
    with db.auto_commit():
        submenu = Submenu()
        submenu.name = form.name.data
        submenu.path = form.path.data
        submenu.pic = form.pic.data
        submenu.menu_id = form.menu_id.data
        submenu.menu_name = menu.menu_name
        submenu.description = form.description.data
        submenu.official_doc = form.official_doc.data
        submenu.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        db.session.add(submenu)
    return Success()
