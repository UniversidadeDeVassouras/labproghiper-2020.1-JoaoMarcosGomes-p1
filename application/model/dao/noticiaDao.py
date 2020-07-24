from application.model.entity.noticia import Noticia
from application import listaNoticia

class NoticiaDao:

    def __init__(self):
        self._listaNoticias = listaNoticias
    def mostrarNoticias(self, estado):
        return estado.getListaNoticias()
    def busca(self, id):
        for noticia in range(0, len(self._listaNoticias)):
            if self._listaNoticias[noticia].getId() == int(id):
                return self._listaNoticias[noticia]
        return None
    def apagarComment(self, noticia):
        noticia.getComment().pop(len(noticia.getComment())-1)
    def salvarView(self, noticia)
        noticia.setQtdView()
    def salvarLike(self, noticia):
        noticia.setQtdLike():