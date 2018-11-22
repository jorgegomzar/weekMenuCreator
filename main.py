import os
from dia import *
from plato import *
import menus as m
import jsonExpert as jE

def crearMenuSemanal():
    """ Encargado de crear un menú a partir de una lista """
    os.system('cls')
    DIAS = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')
    semana = []
    for dia in DIAS:
        d = Dia(dia)
        p1 = Plato('Macarrones', 1, 'Pasta')
        p2 = Plato('Merluza a la plancha', 2, 'Pescado')
        d.addPlato(p1)
        d.addPlato(p2)
        semana.append(d)

    for dia in semana:
        print(dia)

def crearReceta(nombre):
    """ Código empleado en creación de menús, platos y recetarios """
    os.system('cls')
    m.titulizador(nombre)
    nombrePlato = input('Nombre del plato: ')
    while(nombrePlato == ''):
        print('Tienes que introducir un nombre...\n')
        nombrePlato = input('Nombre del plato: ')
    ordenPlato = int(input('Orden del plato (1 o 2): '))
    while(ordenPlato not in [1, 2]):
        print('Tienes que introducir un número...\n')
        ordenPlato = int(input('Orden del plato (1 o 2): '))
    tipoPlato = input('Tipo del plato: ')
    while(tipoPlato == ''):
        print('Tienes que introducir un tipo...\n')
        tipoPlato = input('Tipo del plato: ')
    return {
            "nombre":   nombrePlato,
            "orden":    ordenPlato,
            "tipo":     tipoPlato
            }

def crearRecetario():
    """ Pide la información necesaria al usuario para poder crear un nuevo recetario """
    os.system('cls')
    recetario = []
    nombre_nuevo_recetario = input('Por favor, introduce el nombre del nuevo recetario: ')
    while(True):
        stop = input('¿Parar? (s/otro): ').lower()
        if stop == 's':
            break
        plato = crearReceta(nombre_nuevo_recetario)
        recetario.append(plato)
    jE.crearRecetario(nombre_nuevo_recetario, recetario)

def opcion1(recetario):
    """ Realiza la comprobación de la existencia de recetarios y ejecuta
    la funcion de la primera opcion """
    compr = os.listdir('./recetarios/')
    if len(compr) >= 1:
        crearMenuSemanal()
        os.system('pause')
    else:
        print('No existen recetarios, por favor, crea uno.')
        os.system('pause')

def opcion2():
    """ Realiza la comprobación de la existencia de recetarios y ejecuta
    la funcion de la segunda opcion """
    compr = os.listdir('./recetarios/')
    if len(compr) >= 1:
        crearMenuSemanal()
        os.system('pause')
    else:
        print('No existen recetarios, por favor, crea uno.')
        os.system('pause')

def opcion3(recetario):
    """ Llama a las funciones de MOSTRAR Y AÑADIR, y ELIMINA el recetario """
    compr = os.listdir('./recetarios/')
    if len(compr) >= 1:
        m.mostrarOpcion3(recetario)
        opcion = input('Introduce letra de tu elección: ')
        while(opcion.lower() not in ['a', 'b', 'c']):
            opcion = input('Introduce letra de tu elección: ')
        if opcion == 'a':
            jE.mostrarRecetario(recetario)
        elif opcion == 'b':
            jE.anyadirRecetas(recetario)
        elif opcion == 'c' and recetario.upper() != 'DEFAULT':
            comp = input('¿Estás seguro de querer borrar el recetario {}? (s/otra) \n'.format(recetario.upper()))
            if comp == 's':
                os.remove('./recetarios/'+recetario+'.json')
        else:
            print('El recetario DEFAULT no puede ser borrado.')
            os.system('pause')
    else:
        print('No existen recetarios, por favor, crea uno.')
        os.system('pause')

def opcion4():
    """ Cambia el recetario seleccionado """
    listaRecetarios = []
    lista = os.listdir('./recetarios')
    if len(lista) >= 1:
        os.system('cls')
        print('Recetarios existentes:')
        for item in lista:
            listaRecetarios.append(item.rstrip('json').rstrip('.'))
        for n, item in enumerate(listaRecetarios):
            print ('{} - {}'.format(n+1, item))
        recetario = input('Escribe el nombre completo del que elijas: ')
        while(recetario not in listaRecetarios):
            recetario = input('Escribe el nombre completo del que elijas: ')
    else:
        recetario = 'default'
        print('No existen recetarios, por favor, crea uno.')
        os.system('pause')
    return recetario

if __name__ == "__main__":
    """ Carga los menús """
    recetario = 'default'
    while(True):
        m.menuInicial(recetario)
        opcion = input('\nOpción: ')
        if opcion == '0':     # SALIR OK
            os.system('cls')
            exit()
        elif opcion == '1':     # MENU DESDE RECETARIO
            opcion1(recetario)
        elif opcion == '2':     # MENU DESDE INPUT DE USUARIO
            opcion2()
        elif opcion == '3':     # VER/ AÑADIR / BORRAR
            opcion3(recetario)
        elif opcion == '4':     # CAMBIAR RECETARIO
            recetario = opcion4()
        elif opcion == '5':     # CREAR RECETARIO OK
            crearRecetario()
        else:
            print('Opción no válida.')
            os.system('pause')
