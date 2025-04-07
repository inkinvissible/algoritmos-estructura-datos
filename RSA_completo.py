# === PASO 1: Generar Claves ===
# (Asegúrate de tener p, q, N, e, d definidos)

p = 13
q = 17
N = p * q  # 221
phi = (p - 1) * (q - 1) # 192
e = 7
d = pow(e, -1, phi) # 139

clave_publica = (e, N)
clave_privada = (d, N)

print("--- Claves ---")
print(f"Clave Pública (e, N): {clave_publica}")
print(f"Clave Privada (d, N): {clave_privada}")
print("-" * 30)


# === PASO 2: CIFRADO  ===
mensaje_original = "Hola" 
print("--- CIFRADO ---")
print(f"Mensaje Original: '{mensaje_original}'")

# Convertir CADA caracter a número (M) y cifrarlo individualmente
# El resultado será una LISTA de números cifrados
numeros_cifrados = []
print("Cifrando caracter por caracter:")
for caracter in mensaje_original:
    numero_original = ord(caracter)
    numero_cifrado = pow(numero_original, e, N) # C = M^e mod N
    numeros_cifrados.append(numero_cifrado)
    print(f"  '{caracter}' ({numero_original}) -> Cifrado: {numero_cifrado}")

print(f"\nLista de Números Cifrados (C): {numeros_cifrados} <-- Esto se envía")
print("-" * 30)


# === PASO 4: DESCIFRADO ===
print("--- DESCIFRADO ---")
print(f"Recibimos la lista C={numeros_cifrados}, d={d}, N={N}")

# Descifrar CADA número de la lista y convertirlo de vuelta a caracter
mensaje_descifrado_lista = []
print("Descifrando número por número:")
for num_cifrado in numeros_cifrados:
    numero_descifrado = pow(num_cifrado, d, N) # M = C^d mod N
    caracter_descifrado = chr(numero_descifrado)
    mensaje_descifrado_lista.append(caracter_descifrado)
    print(f"  Número Cifrado {num_cifrado} -> Descifrado: {numero_descifrado} ('{caracter_descifrado}')")

# Unir los caracteres descifrados para formar el mensaje final
mensaje_descifrado = "".join(mensaje_descifrado_lista)
print(f"\nMensaje Descifrado Final: '{mensaje_descifrado}'")
print("-" * 30)
