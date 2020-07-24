from flask import Flask, request
import os
from app.model.entity.estado import Estado
from app.model.dao.estadoDao import EstadoDao
from app.model.entity.noticia import Noticia
from app.model.dao.noticiaDao import NoticiaDao


app = Flask(__name__, static_folder=os.path.abspath("app/view/static"), template_folder=os.path.abspath("app/view/static"))

exnot1 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")
exnot2 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")
exnot3 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")
exnot4 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")
exnot5 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")
exnot6 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "")

listaNoticias = [exnot1,exnot2,exnot3,exnot4,exnot5,exnot6]

exest1 = Estado(1,"Rio de Janeiro", "RJ", 'img/', [exnot1,exnot2])
exest2 = Estado(1,"Rio Grande do Sul", "RS", 'img/', [exnot3,exnot4])
exest3 = Estado(1,"Bahia", "BA", 'img/', [exnot5,exnot6])
listaEstados = [exest1,exest2,exest3]


from app.controller import controllerIndex
from app.controller import controllerEstado
from app.controller import controllerNoticia