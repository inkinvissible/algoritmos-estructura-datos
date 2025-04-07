# Función RECURSIVA para calcular el MCD
def mcd_recursivo(a, b):
    """Calcula el MCD de a y b usando el Algoritmo de Euclides recursivo."""
    print(f"  Llamada con: mcd({a}, {b})")

    # CASO BASE: Si b es 0, el MCD es a. ¡Aquí se detiene la recursión!
    if b == 0:
        print(f"  -> b es 0. El MCD es {a}.")
        return a
    # PASO RECURSIVO: Si b no es 0, llamamos a la misma función pero con 'b' y el 'resto de a dividido por b'.
    else:
        resto = a % b
        print(f"  -> b no es 0. Calculando el resto: {a} % {b} = {resto}")
        print(f"  -> Llamando de nuevo a mcd con ({b}, {resto})")
        return mcd_recursivo(b, resto) # ¡La llamada recursiva!


if __name__ == "__main__":
    num1 = 48
    num2 = 18

    print(f"Calculando el Máximo Común Divisor (MCD) de {num1} y {num2}:")
    resultado = mcd_recursivo(num1, num2)
    print("-" * 30)
    print(f"El MCD final es: {resultado}")