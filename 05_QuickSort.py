# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:36:20 2024

@author: IvanL
"""
# las sublistas.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
lista = [3, 6, 8, 22, 89, 56, 10, 4, 33, 45, 10, 1, 2, 1]
print("Lista desordenada:", lista)
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)