from app import app
from flask import render_template, request
from app.model.dao.estadoDao import EstadoDao
from app.model.entity.estado import Estado


@app.route('/estado/<estado_id>')
def estado(estado_id):
    estadoDao = EstadoDao()
    estado = estadoDao.busca_por_id(estado_id)
    return render_template("estado.html", estado = estado)