import time
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Colores ANSI para terminal ---
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'


# --- Función para mostrar lista en consola ---
def mostrar_lista(arr, current=None, comparar_con=None):
    for i, val in enumerate(arr):
        if i == current:
            print(f"{YELLOW}{BOLD}{val}{RESET}", end=" ")  # Elemento actual
        elif i == comparar_con:
            print(f"{RED}{val}{RESET}", end=" ")  # Elemento con el que se compara
        else:
            print(f"{val}", end=" ")
    print()

# --- Algoritmo de inserción en consola paso a paso ---
def insercion_didactico(arr):
    print(f"{BOLD}Inicio del algoritmo de ordenamiento por inserción:{RESET}")
    print("Lista inicial:")
    mostrar_lista(arr)
    print("\n")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print(f"\n👉 Iteración {i}: Insertar el valor {YELLOW}{key}{RESET} en la parte ordenada.")
        mostrar_lista(arr, current=i)
        time.sleep(1)

        while j >= 0 and arr[j] > key:
            print(f"🔁 {RED}{arr[j]} > {key}{RESET}, entonces movemos {arr[j]} a la derecha")
            arr[j + 1] = arr[j]
            j -= 1
            mostrar_lista(arr, current=i, comparar_con=j)
            time.sleep(1)

        arr[j + 1] = key
        print(f"✅ Insertamos {YELLOW}{key}{RESET} en la posición {j+1}")
        mostrar_lista(arr)
        time.sleep(1)

    print(f"\n{GREEN}{BOLD}Lista ordenada:{RESET}")
    mostrar_lista(arr)

# --- Visualización con matplotlib ---
def animar_insercion(lista_original):
    data = lista_original.copy()
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(data)), data, align="edge", color="skyblue")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def insertion_sort_animated(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            yield data, i, j, f"Seleccionamos {key}"
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
                yield data, i, j, f"Movemos {data[j+1]} a la derecha"
            data[j + 1] = key
            yield data, i, j, f"Insertamos {key} en la posición {j+1}"

    def update(frame):
        array, i, j, mensaje = frame
        for rect, val in zip(bar_rects, array):
            rect.set_height(val)
            rect.set_color("skyblue")
        if i < len(array):
            bar_rects[i].set_color("orange")
        if 0 <= j < len(array):
            bar_rects[j].set_color("red")
        iteration[0] += 1
        text.set_text(f"Paso {iteration[0]}: {mensaje}")

    ani = animation.FuncAnimation(fig, update, frames=insertion_sort_animated(data), interval=1000, repeat=False)
    plt.title("Visualización del algoritmo de inserción")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()

# --- Ejecución principal ---
if __name__ == "__main__":
    lista = [8, 4, 6, 2, 9]
    insercion_didactico(lista.copy())
    input(f"\n{BOLD}Presioná Enter para ver la animación gráfica...{RESET}")
    animar_insercion(lista)
