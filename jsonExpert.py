import json
import os
from menus import titulizador

def crearRecetario(nombre, data):
    """ Crea el archivo json correspondiente al recetario """
    with open('./recetarios/{}.json'.format(nombre), 'w') as new_recetario:
        json.dump(data, new_recetario)

def mostrarRecetario(nombre):
    """ Lee el recetario especificado y lo imprime por pantalla"""
    os.system('cls')
    titulizador('Recetario {}'.format(nombre))
    with open('./recetarios/'+nombre+'.json', 'r') as recetario:
        recetas = json.load(recetario)
        for receta in recetas:
            if receta["orden"] == 1:
                orden = 'Primero'
            else:
                orden = 'Segundo'
            print('- {}: {}, {}'.format(receta["nombre"], orden, receta["tipo"]))
    os.system('pause')

# def anyadirRecetas(nombre):
