class Dia(object):
    def __init__(self, dia):
        self.__dia = dia
        self.__primero = ''
        self.__segundo = ''
    # GET
    def getDay(self):
        return self.__dia
    def getFirst(self):
        return self.__primero
    def getSecond(self):
        return self.__segundo
    # SET
    def setDay(self, dia):
        self.__dia = dia
    def setFirst(self, primero):
        self.__primero = primero
    def setSecond(self, segundo):
        self.__segundo = segundo

    # ADD
    def addPlato(self, plato):
        if plato.getOrder() == 1:
            self.setFirst(plato)
        else:
            self.setSecond(plato)
    # PRINT
    def __str__(self):
        return '{}:\n   Primero: {}\n   Segundo: {}\n'.format(self.__dia, self.__primero.getName(), self.__segundo.getName())
