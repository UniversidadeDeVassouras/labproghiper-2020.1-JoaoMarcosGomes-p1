class Comment:
    def __init__(self, autor, texto):
        self._autor = autor
        self._texto = texto

    def getAutor(self):
        return self._autor
    def getTexto(self):
        return self._texto