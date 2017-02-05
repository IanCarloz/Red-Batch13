# -*- coding: utf-8 -*-

# funciones sin paramentros:

def saludar():
    print('Hola')

saludar()

def saludar_a(nombre):
    print 'Hola ' + nombre

saludar_a('Ian')

# Funciones con valor de retorno
def componer_nombre(nombre, apellido):
    return nombre.capitalize() + ' ' + apellido.capitalize()

nombre_completo = componer_nombre('ian', 'velazquez')

print(nombre_completo)

# Detección de palindromo

def es_palindromo(palabra):
    # True si es palindromo
    # False si no es palindromo
    print('Palabra original: %s' % (palabra))
    palabra = palabra.lower()

    reemplazos = {
        ' ':'',
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u'
    }

    for viejo, nuevo in reemplazos.iteritems():
        palabra = palabra.replace(viejo, nuevo)

    # Quitar espacios
    # palabra = palabra.replace(' ', '')
    # Quitar acentos
    # palabra = palabra.replace('á', 'a')
    # palabra = palabra.replace('é', 'e')
    # palabra = palabra.replace('í', 'i')
    # palabra = palabra.replace('ó', 'o')
    # palabra = palabra.replace('ú', 'u')

    return palabra == palabra[::-1]

print(es_palindromo('Anita Lava la tina'))
