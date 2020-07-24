from flask import render_template, request
from application import app
from application.model.dao.noticiaDao import NoticiaDAO
from application.model.entity.noticia import Noticia
from application.model.dao.estadoDao import EstadoDAO
from application.model.entity.estado import Estado
from application.model.entity.comment import Comment
from application import listaNoticias
from application import listaEstados

@app.route("/noticia/<noticia_id>", methods=['GET'])
def noticia(noticia_id):
    noticiaDao = NoticiaDAO()
    noticia = noticiaDao.busca(noticia_id)
    noticia_dao.armazenar_visualizacao(noticia)
    lista_comentarios = noticia.get_comentarios()
    return render_template("noticia.html", noticia = noticia, listaEstados = listaEstados, listaComments = listaComments)


@app.route('/noticia/<noticia_id>/comments', methods=['POST'])
def comentar(noticia_id):
    noticiaDao = NoticiaDAO()
    noticia = noticiaDao.busca(noticia_id)
    autor = request.values.get('nome') 
    texto = request.values.get('texto')
    comment = Comments(autor, texto)
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

