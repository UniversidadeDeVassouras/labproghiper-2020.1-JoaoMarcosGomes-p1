from flask import render_template, request
from application import app
from application.model.entity.estado import Estado
from application.model.dao.estadoDao import EstadoDAO
from application.model.entity.noticia import Noticia
from application.model.dao.noticiaDao import NoticiaDAO
from application import listaEstados
from application import listaNoticias


@app.route('/')
def home():
    estadoDao = EstadoDAO()
    for estado in listaEstados:
        estado_id = estado.getId()
    estado = estadoDao.busca(estado_id)  

    listaLatest = [listaNoticias[len(listaNoticias)-1], listaNoticias[len(listaNoticias)-2], listaNoticias[len(listaNoticias)-3], listaNoticias[len(listaNoticias)-4]]
    mostLiked = sorted(listaNoticias, key=Noticia.getQtdLike, reverse=True)
    listaMostLiked = [mostLiked[0], mostLiked[1], mostLiked[2], mostLiked[3]]
    
    return render_template("index.html", listaEstados = listaEstados, listaLatest = listaLatest, listaMostLiked = listaMostLiked, estado = estado)
    