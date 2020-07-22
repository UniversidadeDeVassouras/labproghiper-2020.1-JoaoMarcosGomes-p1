from application.model.entity.noticia import Noticia
from application import listaNoticias

class NoticiaDao:

    def __init__(self):
        self._listaNoticias = listaNoticias
    def mostrarEstados(self):
        return self.listaEstados
    def mostrarNoticias(self, estado):
        return estado.getListaNoticias()
    def busca(self, id):
        for estado in range(0, len(self._listaEstados)):
            if self._listaEstados[estado].getId() == int(id):
                return self._listaEstados[estado]
        return None

    def mostrarNoticia(self):
        return self._listaNoticias