from flask import jsonify, request
from sqlalchemy import inspect

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

@api.route('/list/<en_name>')
def get_list(en_name):
    list = Menu.query.filter_by(en_name=en_name).first_or_404()
    return jsonify(list)

@api.route('/sublist/<name>')
def get_sublist(name):
    sublist =Submenu.query.filter_by(name=name).first_or_404()
    sublist.menu_name = sublist.menu.menu_name
    # print(sublist.__dict__)
    return jsonify(sublist)

@api.route('/add/menu', methods=['POST'])
def add_menu():
    form = MenuForm().validate_for_api()
    with db.auto_commit():
        menu = Menu()
        menu.menu_name = form.menu_name.data
        menu.en_name = form.en_name.data
        db.session.add(menu)
    return Success()

@api.route('/add/submenu', methods=['POST'])
def add_submenu():
    form = SubmenuForm().validate_for_api()
    with db.auto_commit():
        submenu = Submenu()
        submenu.name = form.name.data
        submenu.path= form.path.data
        submenu.pic = form.pic.data
        submenu.mid= form.mid.data
        db.session.add(submenu)
    return Success()