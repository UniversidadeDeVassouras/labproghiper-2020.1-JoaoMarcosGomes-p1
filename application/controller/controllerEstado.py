from application import app
from flask import render_template, request
from application.model.dao.estadoDao import EstadoDao
from application.model.entity.estado import Estado


@app.route('/estado/<estado_id>')
def estado(estado_id):
    estadoDao = EstadoDao()
    estado = estadoDao.busca(estado_id)
    return render_template("estado.html", estado = estado)