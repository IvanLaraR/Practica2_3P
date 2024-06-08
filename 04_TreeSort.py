# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:16:33 2024

@author: IvanL
"""

def insertar_en_arbol(arbol, valor):
    if arbol is None:
        return [valor, None, None]  # [valor, izquierda, derecha]
    if valor < arbol[0]:
        arbol[1] = insertar_en_arbol(arbol[1], valor)
    else:
        arbol[2] = insertar_en_arbol(arbol[2], valor)
    return arbol

def recorrido_inorden(arbol, resultado):
    if arbol:
        recorrido_inorden(arbol[1], resultado)
        resultado.append(arbol[0])
        recorrido_inorden(arbol[2], resultado)

def tree_sort(arr):
    if not arr:
        return arr
    
    arbol = None
    for valor in arr:
        arbol = insertar_en_arbol(arbol, valor)
    
    resultado = []
    recorrido_inorden(arbol, resultado)
    return resultado

# Ejemplo de uso
lista = [5, 2, 9, 1, 5, 6, 10, 89, 5, 6, 4, 2]
print("Lista desordenada:", lista)
lista_ordenada = tree_sort(lista)
print("Lista ordenada:", lista_ordenada)