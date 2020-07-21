class Noticia:
    def __init__(self, id, titulo, texto, iconeNoticia, video, dataNoticia, estado):
        self._id = id
        self._titulo = titulo
        self._texto = texto
        self._iconeNoticia = iconeNoticia
        self._video = video
        self._dataNoticia = dataNoticia
        self._estado = estado
        self._qtdView = 0
        self._qtdLike = 0
        self._comments = []

    def getId(self):
        return self._id
    
    def getTitulo(self):
        return self._titulo
    
    def getTexto(self):
        return self._texto
    
    def getIconeNoticia(self):
        return self._iconeNoticia
    
    def getVideo(self):
        return self._id
    
    def getDataNoticia(self):
        return self._id
    
    def getEstado(self):
        return self._id
    
    def setQtdView(self):
        self._qtdView = self._qtdView + 1
    
    def getQtdView(self):
        return self._qtdView

    def setQtdLike(self):
        self._qtdLike = self._qtdLike + 1
    
    def getQtdLike(self):
        return self._qtdLike 

    def setComment(self,comment):
        self._comments.append(comment)
    
    def getComment(self):
        return self._comments