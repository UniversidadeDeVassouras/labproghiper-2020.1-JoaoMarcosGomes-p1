from application.model.entity.estado import Estado
from application import listaEstados

class EstadoDao:
    def __init__(self):
        self._listaEstados = listaEstados
    def mostrarEstados(self):
        return self._listaEstados
    def mostrarNoticias(self, estado):
        return estado.getListaNoticias()
    def busca(self, id):
        for estado in range(0, len(self._listaEstados)):
            if self._listaEstados[estado].getId() == int(id):
                return self._listaEstados[estado]
        return None