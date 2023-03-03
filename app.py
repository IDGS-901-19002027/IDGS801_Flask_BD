from flask import Flask 
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

import forms 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.nombre.data,
                       email = create_form.email.data
        )
        # Insert en la BD
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form = create_form)

if __name__ == '__main__':
    # Aplicar la seguridad CSRF al inicializar la aplicación
    csrf.init_app(app)
    # Objeto para la manipulación de la BD
    db.init_app(app)
    # Comprueba si la BD existe y genera un mapeo en automático de las tablas
    with app.app_context():
        db.create_all()
    app.run(port=3000)