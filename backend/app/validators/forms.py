from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(message='账号不能为空'), length(
        min=5, max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='邮箱格式不正确')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class BookSearchForm(BaseForm):
    q = StringField(validators=[DataRequired()])


class TokenForm(BaseForm):
    token = StringField(validators=[DataRequired()])


class MenuForm(BaseForm):
    menu_name = StringField(validators=[DataRequired()])
    en_name = StringField(validators=[DataRequired()])


class SubmenuForm(BaseForm):
    name = StringField(validators=[DataRequired()])
    path = StringField(validators=[DataRequired()])
    pic = StringField(validators=[DataRequired()])
    mid = IntegerField(validators=[DataRequired()])


