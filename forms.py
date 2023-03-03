from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo')
