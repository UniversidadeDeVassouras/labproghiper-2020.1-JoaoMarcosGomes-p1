class Estado:
    def __init__(self, id, nome, uf, iconeEstado, listaNoticias):
        self._id = id
        self._nome = nome
        self._uf = uf
        self._iconeEstado = iconeEstado
        self._listaNoticias = listaNoticias

    def getId(self):
        return self._id
    def getNome(self):
        return self._nome
    def getUf(self):
        return self._uf
    def getIcone(self):
        return self._iconeEstado
    def getNewsList(self):
        return self._listaNoticias