# -*- coding: utf-8 -*-

# Funciones
batch_13 = [
    {'nombre':'antonio', 'edad':41},
    {'nombre':'Ximena', 'edad':24}
]
batch_x = [
    {'nombre':'toño', 'edad':40},
    {'nombre':'Xime', 'edad':20}
]
batchhh = [
    {'nombre':'toño', 'edad':40},
    {'nombre':'Xime', 'edad':20},
    {'name':'guy', 'age':0}
]
def imprimir_grupo(grupo):

    for alumno in grupo:
        for dato, valor in alumno.iteritems():
            print( dato + " : " + str(valor))

lista = [1, 2 , 3, 4, 5]
lista2 = [{'a':1, 'b':2 , 'c':3, 'd':4, 'e':5},{1:'a', 2:'b', 3:'c'}]

def funcion(algo):
    for otro_algo in algo:
        for value in otro_algo:
            print value

def tercera(esto):


#imprimir_grupo(batchhh)
#funcion(lista2)
