from flask import render_template, request
from app import app
from app.model.dao.noticiaDao import NoticiaDAO
from app.model.entity.noticia import Noticia
from app.model.dao.estadoDao import EstadoDAO
from app.model.entity.estado import Estado
from app.model.entity.comment import Comment
from app import listaNoticias
from app import listaEstados

@app.route("/noticia/<noticia_id>", methods=['GET'])
def noticia(noticia_id):
    noticiaDao = NoticiaDAO()
    noticia = noticiaDao.busca(noticia_id)
    noticiaDao.armazenar_visualizacao(noticia)
    lista_comentarios = noticia.get_comentarios()
    return render_template("noticia.html", noticia = noticia, listaEstados = listaEstados, listaComments = listaComments)


@app.route('/noticia/<noticia_id>/comments', methods=['POST'])
def comentar(noticia_id):
    noticiaDao = NoticiaDAO()
    noticia = noticiaDao.busca(noticia_id)
    autor = request.values.get('nome') 
    texto = request.values.get('texto')
    comment = Comment(autor, texto)
    noticia.setComment(comment)
    return render_template('comments.html', noticia = noticia), 201

@app.route("/noticia/<noticia_id>/curtir", methods=['POST'])
def curtir(noticia_id):
    noticiaDao = NoticiaDAO()
    noticia = noticiaDao.busca(noticia_id)
    noticiaDao.salvarLike(noticia)
    return render_template("curtidas.html", noticia = noticia), 200

@app.route('/noticia/<noticia_id>/comments', methods=['DELETE'])
def apagar(noticia_id):
    noticiaDao = NoticiaDAO()
    noticia = noticiaDao.busca(noticia_id)
    noticiaDao.apagarComment(noticia)
    return render_template('comments.html', noticia = noticia), 200

