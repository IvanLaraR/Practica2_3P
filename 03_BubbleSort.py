# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:49:29 2024

@author: IvanL
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 56, 59, 66, 47, 102, 22, 11, 90, 102, 200]
print("Lista desordenada:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)