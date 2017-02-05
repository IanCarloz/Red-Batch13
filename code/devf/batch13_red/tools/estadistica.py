# -*- coding: utf-8 -*-

# lista_valores = [10, 100, 90.9 100]
# suma_total / numero_elementos
def promedio():
    promedio = sum(lista_valores) / len(lista_valores)
    return promedio

def moda(lista_valores):
    valores = {}
    for valor in lista_valores:
        if valores.get(valor):
            valores[valor] += 1
        else:
            valores[valor] = 1

    # print(valores)

    v_max = 0
    moda = 0

    for valor, repeticiones in valores.iteritems():
        if repeticiones > v_max:
            v_max = repeticiones
            moda = valor

    return moda

def mediana(lista_valores):
    # ordenar lista
    # detect par 
    lista_valores.sort()
    if len(lista_valores) % 2:

    return mediana

lista_valores = [100, 300, 100, 4 ]
print(moda(lista_valores))
