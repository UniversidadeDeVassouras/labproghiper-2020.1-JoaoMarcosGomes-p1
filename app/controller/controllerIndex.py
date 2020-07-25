from flask import render_template, request
from app import app
from app.model.entity.estado import Estado
from app.model.dao.estadoDao import EstadoDAO
from app.model.entity.noticia import Noticia
from app.model.dao.noticiaDao import NoticiaDAO
from app import listaEstados
from app import listaNoticias


@app.route('/')
def home():
    estadoDao = EstadoDAO()
    for estado in listaEstados:
        estado_id = estado.getId()
    estado = estadoDao.busca_por_id(estado_id)  
    listaLatest = [listaNoticias[len(listaNoticias)-1], listaNoticias[len(listaNoticias)-2], listaNoticias[len(listaNoticias)-3], listaNoticias[len(listaNoticias)-4]]
    mostLiked = sorted(listaNoticias, key=Noticia.getQtdLike, reverse=True)
    listaMostLiked = [mostLiked[0], mostLiked[1], mostLiked[2], mostLiked[3]]
    return render_template("index.html", listaEstados = listaEstados, listaLatest = listaLatest, listaMostLiked = listaMostLiked, estado = estado)
    
