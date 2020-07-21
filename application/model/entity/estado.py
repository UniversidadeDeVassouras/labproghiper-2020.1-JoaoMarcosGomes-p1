class Estado:
    def __init__(self, id, nome, uf, iconeEstado, newslist):
        self._id = id
        self._nome = nome
        self._uf = uf
        self._icone = icone
        self._newslist = newslist

    def getId(self):
        return self._id
    def getNome(self):
        return self._nome
    def getUf(self):
        return self._uf
    def getIcone(self):
        return self._iconeEstado
    def getNewsList(self):
        return self._newslist