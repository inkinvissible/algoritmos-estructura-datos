import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

# ─────────────────────────────
# Colores ANSI para la consola (solo se usan en la parte didáctica en consola)
# ─────────────────────────────
RED = '\033[91m'       
GREEN = '\033[92m'     
YELLOW = '\033[93m'    
RESET = '\033[0m'      
BOLD = '\033[1m'       

# ─────────────────────────────
# Colores para la animación (nombres válidos para matplotlib)
# ─────────────────────────────
plot_skyblue = "skyblue"
plot_red = "red"
plot_yellow = "yellow"
plot_lightgray = "lightgray"
plot_box_color = "black"  # Color para el recuadro del subarreglo

# ─────────────────────────────
# Función para mostrar el arreglo en consola (sin modificaciones)
# ─────────────────────────────
def mostrar_lista(arr, low=None, high=None, pivot_index=None, current=None):
    for i, val in enumerate(arr):
        if pivot_index is not None and i == pivot_index:
            print(f"{YELLOW}{BOLD}{val}{RESET}", end=" ")
        elif current is not None and i == current:
            print(f"{RED}{val}{RESET}", end=" ")
        elif low is not None and high is not None and low <= i <= high:
            print(f"{val}", end=" ")
        else:
            print(f"{val}", end=" ")
    print()

# ─────────────────────────────
# Algoritmo de Quicksort – Versión didáctica para consola
# (Se mantiene igual que antes)
# ─────────────────────────────
def quicksort_didactico(arr, low, high, depth=0):
    indent = "  " * depth
    if low < high:
        print(f"{indent}{BOLD}Procesando subarreglo de índices {low} a {high}:{RESET}")
        print(f"{indent}Estado actual:")
        mostrar_lista(arr, low, high)
        time.sleep(1)
        
        pivot_index = particionar_didactico(arr, low, high, depth)
        
        print(f"{indent}{GREEN}Pivote colocado en la posición {pivot_index}{RESET}")
        mostrar_lista(arr, low, high, pivot_index=pivot_index)
        time.sleep(1)
        
        quicksort_didactico(arr, low, pivot_index - 1, depth + 1)
        quicksort_didactico(arr, pivot_index + 1, high, depth + 1)
    else:
        if low == high:
            print(f"{indent}Subarreglo de un solo elemento en índice {low}: {arr[low]}")
            time.sleep(0.5)
        return

def particionar_didactico(arr, low, high, depth):
    indent = "  " * depth
    pivot = arr[high]
    print(f"{indent}Pivote seleccionado: {YELLOW}{pivot}{RESET} (índice {high})")
    i = low - 1
    for j in range(low, high):
        print(f"{indent}Comparando {arr[j]} (índice {j}) con el pivote {pivot}")
        if arr[j] <= pivot:
            i += 1
            print(f"{indent}{RED}Intercambiamos{RESET} {arr[i]} (índice {i}) con {arr[j]} (índice {j})")
            arr[i], arr[j] = arr[j], arr[i]
            mostrar_lista(arr, low, high, pivot_index=high, current=j)
            time.sleep(1)
        else:
            print(f"{indent}No se intercambia {arr[j]} (índice {j}), es mayor que el pivote.")
            time.sleep(0.5)
    print(f"{indent}Colocamos el pivote {pivot} en la posición {i+1}")
    arr[i+1], arr[high] = arr[high], arr[i+1]
    mostrar_lista(arr, low, high, pivot_index=i+1)
    time.sleep(1)
    return i + 1

# ─────────────────────────────
# Animación de Quicksort con matplotlib (versión avanzada y explicativa)
# ─────────────────────────────
def quicksort_animated(arr, low, high):
    """
    Función generadora para Quicksort.
    Cada frame es una tupla de 7 elementos:
      (copia del arreglo, low, high, pivote, índice actual, mensaje, swap_info)
    swap_info es una tupla (source, target) si se realizó un intercambio, sino None.
    """
    if low < high:
        pivot_index = yield from particionar_animated(arr, low, high)
        yield from quicksort_animated(arr, low, pivot_index - 1)
        yield from quicksort_animated(arr, pivot_index + 1, high)
    else:
        yield (arr.copy(), low, high, None, None, f"Subarreglo [{low}, {high}] ya ordenado.", None)

def particionar_animated(arr, low, high):
    pivot = arr[high]
    # Frame inicial: se selecciona el pivote
    yield (arr.copy(), low, high, pivot, None, f"Pivote seleccionado: {pivot} (índice {high})", None)
    i = low - 1
    for j in range(low, high):
        # Frame: comparación del elemento en j con el pivote
        yield (arr.copy(), low, high, pivot, j, f"Comparando {arr[j]} (índice {j}) con pivote {pivot}", None)
        if arr[j] <= pivot:
            i += 1
            # Realizamos el intercambio y generamos un frame con información de la flecha (desde j hasta i)
            arr[i], arr[j] = arr[j], arr[i]
            yield (arr.copy(), low, high, pivot, j, f"Intercambio: movemos {arr[i]} (índice {i}) a la izquierda", (j, i))
    # Intercambio final: colocar el pivote en su posición correcta
    arr[i+1], arr[high] = arr[high], arr[i+1]
    yield (arr.copy(), low, high, pivot, i+1, f"Colocamos pivote {pivot} en su posición {i+1}", (high, i+1))
    return i + 1

# Variables globales para la animación
bar_rects = None
text = None
subarray_box = None
arrow_annotation = None

def update(frame):
    """
    Función de actualización para la animación.
    Se actualizan:
      - Las barras (array).
      - Se dibuja un recuadro alrededor del subarreglo actual.
      - Se dibuja una flecha si hay un intercambio.
      - Se muestra un mensaje explicativo.
    """
    global subarray_box, arrow_annotation
    array, low, high, pivot, current, message, swap_info = frame

    # Actualizamos todas las barras
    for rect, val in zip(bar_rects, array):
        rect.set_height(val)
        rect.set_color(plot_skyblue)

    # Resaltamos el subarreglo actual con un recuadro (borramos el anterior si existe)
    ax = bar_rects[0].axes
    if subarray_box is not None:
        subarray_box.remove()
    # Calculamos la posición y ancho para el recuadro
    x = low - 0.4
    width = high - low + 1 + 0.8
    subarray_box = Rectangle((x, 0), width, max(array)*1.1, linewidth=2, edgecolor=plot_box_color, facecolor='none', linestyle='--')
    ax.add_patch(subarray_box)

    # Resaltamos el pivote (último elemento del subarreglo) con color amarillo
    if pivot is not None:
        bar_rects[high].set_color(plot_yellow)
    
    # Resaltamos el elemento actual en rojo, si corresponde
    if current is not None and low <= current <= high:
        bar_rects[current].set_color(plot_red)
    
    # Si hay información de intercambio, dibujamos una flecha
    if arrow_annotation is not None:
        arrow_annotation.remove()
        arrow_annotation = None
    if swap_info is not None:
        source, target = swap_info
        # Coordenadas de la flecha: desde el centro superior de la barra "source" hasta la barra "target"
        x_source = bar_rects[source].get_x() + bar_rects[source].get_width()/2
        y_source = bar_rects[source].get_height()
        x_target = bar_rects[target].get_x() + bar_rects[target].get_width()/2
        y_target = bar_rects[target].get_height()
        arrow_annotation = ax.annotate("",
            xy=(x_target, y_target), xycoords='data',
            xytext=(x_source, y_source+0.5), textcoords='data',
            arrowprops=dict(arrowstyle="->", color="black", lw=2))
    
    text.set_text(message)

# ─────────────────────────────
# Función para animar Quicksort con matplotlib (versión avanzada)
# ─────────────────────────────
def animar_quicksort(lista_original):
    data = lista_original.copy()
    global bar_rects, text, subarray_box, arrow_annotation
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(data)), data, align="edge", color=plot_skyblue)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, color="black")
    
    # Inicializamos variables para el recuadro y la flecha
    subarray_box = None
    arrow_annotation = None
    
    gen = quicksort_animated(data, 0, len(data)-1)
    ani = animation.FuncAnimation(fig, update, frames=gen, interval=2000, repeat=False)
    
    plt.title("Visualización de Quicksort")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()

# ─────────────────────────────
# Programa principal
# ─────────────────────────────
if __name__ == "__main__":
    # Lista de ejemplo para Quicksort
    lista = [8, 4, 7, 3, 10, 2]
    
    # Parte 1: Demostración didáctica en consola (se mantiene igual)
    print(f"{BOLD}--- Demostración de Quicksort en Consola ---{RESET}")
    print("Lista inicial:")
    mostrar_lista(lista)
    time.sleep(1)
    quicksort_didactico(lista, 0, len(lista) - 1)
    print(f"\n{GREEN}{BOLD}Lista ordenada:{RESET}")
    mostrar_lista(lista)
    
    # Espera a que el usuario presione Enter para pasar a la animación gráfica
    input(f"\n{BOLD}Presioná Enter para ver la animación gráfica de Quicksort...{RESET}")
    
    # Parte 2: Animación gráfica con matplotlib
    lista_anim = [8, 4, 7, 3, 10, 2]  # Reiniciamos la lista para la animación
    animar_quicksort(lista_anim)
