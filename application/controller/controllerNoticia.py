from application import app
from flask import render_template, request
from application.model.dao.noticiaDao import NoticiaDao
from application.model.entity.noticia import Noticia

noticiaDao = NoticiaDao()

