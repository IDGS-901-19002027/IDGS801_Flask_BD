from wtforms import Form
from wtforms import StringField, IntegerField, SelectField, RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo')

class FormResistencias(Form):
    colores1 = [('', 'Seleccione una opción'),('0', 'Negro'), ('1', 'Café'), ('2', 'Rojo'), ('3', 'Naranja'), ('4', 'Amarillo'), 
              ('5', 'Verde'), ('6', 'Azul'), ('7', 'Violeta'), ('8', 'Gris'), ('9', 'Blanco')]
    colores2 = [('', 'Seleccione una opción'),('1', 'Negro'), ('10', 'Café'), ('100', 'Rojo'), 
                ('1000', 'Naranja'), ('10000', 'Amarillo'), ('100000', 'Verde'), ('1000000', 'Azul'), 
                ('10000000', 'Violeta'), ('100000000', 'Gris'), ('1000000000', 'Blanco')]
    
    banda1 = SelectField('Primera banda:', choices = colores1, validators = [validators.InputRequired('Debe seleccionar una opción')])
    banda2 = SelectField('Segunda banda:', choices = colores1, validators=[validators.InputRequired('Debe seleccionar una opción')])
    banda3 = SelectField('Tercera banda:', choices = colores2, validators = [validators.InputRequired('Debe seleccionar una opción')])
    tolerancia = RadioField('Tolerancias', choices = [('gold', 'ORO 5%'), ('silver', 'PLATA 10%')], 
                            validators = [validators.InputRequired(message='Seleccione una tolerancia')])