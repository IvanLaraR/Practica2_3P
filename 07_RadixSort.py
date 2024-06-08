# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:26:59 2024

@author: IvanL
"""

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contar ocurrencias de dígitos
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Cambiar count[i] para que contenga la posición de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el array de salida a arr[], para que arr[] contenga los números ordenados según el dígito actual
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el número con el mayor número de dígitos
    max_num = max(arr)
    
    # Realizar Counting Sort para cada dígito
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
lista = [170, 45, 75, 90, 802, 24, 10, 77, 25]
print("Lista desordenada:", lista)
radix_sort(lista)
print("Lista ordenada:", lista)