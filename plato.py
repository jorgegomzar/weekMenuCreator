class Plato(object):
    def __init__(self, nombre, orden, tipo): # Constructor de la clase
        self.__nombre = nombre
        self.__orden = orden
        self.__tipo = tipo
    # GET
    def getName(self):
        return self.__nombre
    def getOrder(self):
        return self.__orden
    def getType(self):
        return self.__tipo
    # SET
    def setName(self, nuevoNombre):
        self.__nombre = nuevoNombre
    def setOrder(self, nuevoOrden):
        self.__orden = nuevoOrden
    def setType(self, nuevoTipo):
        self.__tipo = nuevoTipo
    # PRINT
    def __str__(self):
        orden = ''
        if self.__orden == 1:
            orden = 'Primero'
        else:
            orden = 'Segundo'
        return '{}: {}, {}'.format(self.__nombre, orden, self.__tipo)
