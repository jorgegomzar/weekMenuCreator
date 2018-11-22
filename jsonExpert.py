import json
import os
from menus import titulizador
import plato as p

def crearRecetario(nombre, data):
    """ Crea el archivo json correspondiente al recetario """
    with open('./recetarios/{}.json'.format(nombre), 'w') as new_recetario:
        json.dump(data, new_recetario)

def mostrarRecetario(nombre):
    """ Lee el json especificado y lo imprime por pantalla"""
    os.system('cls')
    titulizador('Recetario {}'.format(nombre))
    print('[+] A continuación se muestran todos los platos del recetario:')
    listaPlatos = leerRecetarioPlatos(nombre)
    for plato in listaPlatos:
        print(plato)
    os.system('pause')

def leerRecetario(nombre):
    """ Abre el fichero json, lo lee y devuelve los platos """
    listaPlatos = []
    with open('./recetarios/'+nombre+'.json', 'r') as recetario:
        recetas = json.load(recetario)
        for receta in recetas:
            plato = {
                    "nombre":   receta["nombre"],
                    "orden":    receta["orden"],
                    "tipo":     receta["tipo"]
                    }
            listaPlatos.append(plato)
        return listaPlatos

def leerRecetarioPlatos(nombre):
    """ Abre el fichero json, lo lee y devuelve los platos """
    listaPlatos = []
    with open('./recetarios/'+nombre+'.json', 'r') as recetario:
        recetas = json.load(recetario)
        for receta in recetas:
            plato = p.Plato(receta["nombre"], receta["orden"], receta["tipo"])
            listaPlatos.append(plato)
        return listaPlatos
