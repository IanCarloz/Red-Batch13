# -*- coding: utf-8 -*-

batch_13 = ["Alejandro", "Franck", "Sebastian", "Nelly", "Cynthia"]

elementos = 'aire', 'viento', 'tierra', 'fuego'

# Iterables

# for elemento_individual in iterable:
#   le hago algo
for alumno in batch_13:
    print(alumno)
# Range [1, ...]
# Range [inicio, fin(exlusivo), step(opcional)]
for i in range(1, 10, 1):
    print(i)

for elemento in elementos:
    print(elemento)

persona = {
    'nombre':'Ian',
    'apellido':'Velazquez',
    'edad':27
}

personas = [{
    'nombre':'Ian',
    'apellido':'Velazquez',
    'edad':27
},{
    'nombre':'Pedro',
    'apellido':'Perez',
    'edad':100
}]

print('Dicionario - - - - - - - -')

for dato, valor in persona.iteritems():
    print(dato + ": " + str(valor))
