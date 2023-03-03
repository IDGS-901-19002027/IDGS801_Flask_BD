from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    # Asignar el nombre de la tabla
    __tablename__ = "alumnos"
    # Asignar los campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(100))
    email = db.Column(db.String(50))
    # Crear otro campo para la guardar la fecha de registro de un usuario
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
    
