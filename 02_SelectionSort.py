# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:22:10 2024

@author: IvanL
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
lista = [64, 99, 26, 10, 50, 89, 1025, 25, 12, 22, 11]
print("Lista desordenada:", lista)
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)
