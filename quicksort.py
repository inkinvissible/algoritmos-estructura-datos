def quicksort(arr):
    # Caso base: Si la lista tiene 0 o 1 elemento, ya está ordenada.
    if len(arr) <= 1:
        return arr
    
    # Seleccionar el pivote: se elige el elemento central
    pivot = arr[len(arr) // 2]
    
    # Dividir la lista en tres sublistas:
    # - 'left' contiene elementos menores que el pivote.
    # - 'middle' contiene elementos iguales al pivote.
    # - 'right' contiene elementos mayores que el pivote.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Aplicar recursivamente QuickSort en las sublistas y combinarlas.
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso:
lista = [3, 6, 8, 10, 1, 2, 1]
print("Lista ordenada:", quicksort(lista))
# Salida esperada: Lista ordenada: [1, 1, 2, 3, 6, 8, 10]
# Este código implementa el algoritmo QuickSort de manera recursiva.
# Elige un pivote, divide la lista en tres partes y ordena recursivamente.
# QuickSort es eficiente y tiene un tiempo de ejecución promedio de O(n log n).
# Sin embargo, en el peor de los casos, su tiempo de ejecución puede ser O(n^2).

# Para ver visualmente lo que hace el algoritmo, dirigirse a https://pythontutor.com/render.html#mode=display