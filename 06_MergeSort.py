# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:57:55 2024

@author: IvanL
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Ejemplo de uso
lista = [38, 27, 43, 88, 10, 45, 71, 33, 30, 3, 9, 82, 10]
print("Lista desordenada:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)
