class Estado:
    def __init__(self, id, nome, sigla, iconeEstado, listaNoticias):
        self._id = id
        self._nome = nome
        self._sigla = sigla
        self._iconeEstado = iconeEstado
        self._listaNoticias = listaNoticias

    def getId(self):
        return self._id
    def getNome(self):
        return self._nome
    def getSigla(self):
        return self._sigla
    def getIcone(self):
        return self._iconeEstado
    def getNewsList(self):
        return self._listaNoticias