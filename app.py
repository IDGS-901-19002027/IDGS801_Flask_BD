from flask import Flask 
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from flask import make_response

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

@app.route("/ABCompleto", methods=['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    # Select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from alumnos where id==id    
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id = create_form.id.data
        # Select * from alumnos where id==id    
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html', form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from alumnos where id==id    
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id = create_form.id.data
        # Select * from alumnos where id==id    
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html', form=create_form)

@app.route('/resistencias', methods=['GET', 'POST'])
def resistencias():
    reg_resistencias = forms.FormResistencias(request.form)
    btnAgregar = request.form.get('btnAgregar')
    btnLeerArchivo = request.form.get('btnLeerArchivo')
    mostrarTabla = False
    coloresBanda = {"0": "black", "1": "brown", "2": "red", "3": "orange", "4": "yellow", "5": "green", "6": "blue",
                    "7": "purple", "8": "gray", "9": "white"}
    coloresBandaMultiplicadora = {"1": "black", "10": "brown", "100": "red", "1000": "orange", "10000": "yellow", "100000": "green",
                                  "1000000": "blue", "10000000": "purple", "100000000": "gray", "1000000000": "white"}
    coloresTolerancia = {"gold": "gold", "silver": "silver"}
    valoresTolerancia = {"gold": "5", "silver": "10"}
    seleccionBanda1 = ""
    seleccionBanda2 = ""
    seleccionBandaMulti = ""
    seleccionTolerancia = ""
    valorHexBanda1 = []
    valorHexBanda2 = []
    valorHexBandaMulti = []
    valorHexTolerancia = []
    valorResistencia = []
    tolerancia = []
    maxValor = []
    minValor = []
    cantidadLineas = 0
    lineas = 0

    if (request.method == "POST" and reg_resistencias.validate()):
        if (btnAgregar == "btnAgregar"):
            seleccionBanda1 = reg_resistencias.banda1.data
            seleccionBanda2 = reg_resistencias.banda2.data
            seleccionBandaMulti = reg_resistencias.banda3.data
            seleccionTolerancia = reg_resistencias.tolerancia.data

            with open('resistencias.txt', 'a') as f:
                f.write(f'{coloresBanda[seleccionBanda1]},{coloresBanda[seleccionBanda2]},{coloresBandaMultiplicadora[seleccionBandaMulti]},{coloresTolerancia[seleccionTolerancia]}\n')

        if (btnLeerArchivo == "btnLeerArchivo"):
            mostrarTabla = True
            archivo = open('resistencias.txt', 'r')
            datos = archivo.readlines()
            lineas = []
            valBanda1 = []
            valBanda2 = []
            valBanda3 = []
            valTolerancias = []

            for n in datos:
                lineas.append(n.replace('\n', '')) 

            cantidadLineas = len(lineas)

            for color in lineas:
                elemento1 = color.split(',')[0].strip()
                elemento2 = color.split(',')[1].strip()
                elemento3 = color.split(',')[2].strip()
                elemento4 = color.split(',')[3].strip()
                valorHexBanda1.append(elemento1)
                valorHexBanda2.append(elemento2)
                valorHexBandaMulti.append(elemento3)
                valorHexTolerancia.append(elemento4)

            for color in valorHexBanda1:
                for clave, valor in coloresBanda.items():
                    if valor == color:
                        valBanda1.append(clave)

            for color in valorHexBanda2:
                for clave, valor in coloresBanda.items():
                    if valor == color:
                        valBanda2.append(clave)

            for color in valorHexBandaMulti:
                for clave, valor in coloresBandaMultiplicadora.items():
                    if valor == color:
                        valBanda3.append(clave)

            for clave in valorHexTolerancia:
                valTolerancias.append(valoresTolerancia[clave])

            for n in range(cantidadLineas):
                valorResistencia.append(int(valBanda1[n] + valBanda2[n]) * int(valBanda3[n]))
                tolerancia.append(valorResistencia[n] * (int(valTolerancias[n]) / 100))
                maxValor.append(valorResistencia[n] + tolerancia[n])
                minValor.append(valorResistencia[n] - tolerancia[n])

                if (valorResistencia[n] >= 1000 and valorResistencia[n] < 1000000):
                    valorResistencia[n] = "{}k ".format(str(valorResistencia[n] / 1000))
                    maxValor[n] = "{}k ".format(str(maxValor[n] / 1000))
                    minValor[n] = "{}k ".format(str(minValor[n] / 1000))

                elif (valorResistencia[n] >= 1000000 and valorResistencia[n] < 1000000000):
                    valorResistencia[n] = "{}M ".format(str(valorResistencia[n] / 1000000))
                    maxValor[n] = "{}M ".format(str(maxValor[n] / 1000000))
                    minValor[n] = "{}M ".format(str(minValor[n] / 1000000))

                elif(valorResistencia[n] >= 1000000000):
                    valorResistencia[n] = "{}G ".format(str(valorResistencia[n] / 1000000000))
                    maxValor[n] = "{}G ".format(str(maxValor[n] / 1000000000))
                    minValor[n] = "{}G ".format(str(minValor[n] / 1000000000)) 
                

    response = make_response(render_template('resistencias.html', form = reg_resistencias, valorHexBanda1 = valorHexBanda1, valorHexBanda2 = valorHexBanda2, 
                                             valorHexBandaMulti = valorHexBandaMulti, valorHexTolerancia = valorHexTolerancia, valorResistencia = valorResistencia,
                                             maxValor = maxValor, minValor = minValor, cantidadLineas = cantidadLineas, mostrarTabla = mostrarTabla))
    response.set_cookie('valorResistencia', str(valorResistencia))
    response.set_cookie('maxValor', str(maxValor))
    response.set_cookie('minValor', str(minValor))
    return response


if __name__ == '__main__':
    # Aplicar la seguridad CSRF al inicializar la aplicación
    csrf.init_app(app)
    # Objeto para la manipulación de la BD
    db.init_app(app)
    # Comprueba si la BD existe y genera un mapeo en automático de las tablas
    with app.app_context():
        db.create_all()
    app.run(port=3000)