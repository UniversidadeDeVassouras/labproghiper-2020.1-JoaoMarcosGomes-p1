from flask import Flask, request
from application.model.entity.estado import Estado
from application.model.dao.estadoDao import EstadoDao
from application.model.entity.noticia import Noticia
from application.model.dao.noticiaDao import NoticiaDao
import os

app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

exnot1 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")
listaNoticias = [exnot1]

exest1 = Estado(1,"Rio de Janeiro", "RJ", 'img/', [exnot1])
listaEstados = [exest1]


