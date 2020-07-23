from application import app
from flask import render_template, request
from application.model.dao.estadoDao import EstadoDao
from application.model.entity.estado import Estado

estadoDao = EstadoDao()

@app.route('/', methods=['GET'])
def home():
    