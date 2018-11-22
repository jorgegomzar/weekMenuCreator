import os

def menuInicial(recetario):
    """" Muestra la primera pantalla """
    os.system('cls')
    titulizador('Week Menu Creator!')
    recetarioActual(recetario)
    indexizador('1.- Crear menú desde recetario.')              #
    indexizador('2.- Crear menú personalizado.')                #
    indexizador('3.- Ver/Añadir/Borrar recetario actual.')      # Falta AÑADIR
    indexizador('4.- Seleccionar otro recetario.')              # OK
    indexizador('5.- Crear un recetario nuevo.')                #
    print(format('','-^70'))
    indexizador('0.- Salir.')                                   # OK
    print(format('','-^70'))

def recetarioActual(nombre):
    """" Muestra en un rótulo la receta actual en la primera pantalla """
    print('|', format('Recetario: {}'.format(nombre).upper(), '^66'),'|')
    print(format('|','-<68'), '|')

def mostrarOpcion3(recetario):
    """ Muestra la pantalla para la opcion 3 """
    os.system('cls')
    titulizador('Modificar recetario')
    indexizador('a) Ver recetario {}'.format(recetario.upper()))
    indexizador('b) Añadir al recetario {}'.format(recetario.upper()))
    indexizador('c) Eliminar recetario {}'.format(recetario.upper()))
    print(format('','-^70'))

# -------------- FUNCIONES AUXILIARES --------------
def espaciador(texto):
    """" Formatea cadenas de texto añadiendo espacios """
    salida = ''
    for caracter in texto:
        salida = salida + caracter
        salida = salida + ' '
    return salida

def titulizador(texto):
    """" Formatea títulos """
    texto = espaciador(texto)
    print(format('','-^70'))
    print(format('|','<68'), '|')
    print('|',format(texto.upper(), '^66'), '|')
    print(format('|','<68'), '|')
    print(format('','-^70'))

def indexizador(texto):
    """" Formatea indices """
    print(format('|','<68'), '|')
    print('|',format(texto, '<66'), '|')
