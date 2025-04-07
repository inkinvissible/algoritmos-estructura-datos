# === PASO 1: Elegir números ===

# Imagina que elegimos dos primos secretos pequeños: p=13, q=17
# (En la vida real son ENORMES y aleatorios)
p = 13
q = 17

# Calcular N (Parte Pública)
N = p * q  # N = 13 * 17 = 221

# Calcular "phi" (Secreto, necesario para 'd')
phi = (p - 1) * (q - 1) # phi = 12 * 16 = 192

# Elegir 'e' (Parte Pública)
# Debe ser 1 < e < phi y no compartir factores con phi.
e = 7

# Calcular 'd' (Parte Privada - ¡La Magia!)
# Necesitamos que (d * e) % phi == 1
# Python lo calcula fácil 
d = pow(e, -1, phi) # d = pow(7, -1, 192) que da 139

# --- ¡Tenemos las Claves! ---
print("--- GENERACIÓN DE CLAVES (Simplificada) ---")
print(f"Valor N (Público): {N}")
print(f"Valor e (Público): {e}")
print(f"Valor d (Privado): {d} <-- ¡ESTE ES EL SECRETO!")
print("-" * 30)

# === PASO 2: CIFRADO ===
mensaje_original = "C" # ¡Un solo caracter para máxima simpleza!
print("--- CIFRADO ---")
print(f"Mensaje Original: '{mensaje_original}'")

# Convertir el caracter a número (M)
numero_original = ord(mensaje_original)
print(f"Mensaje como Número (M): {numero_original}")

# Fórmula de Cifrado: C = M^e mod N
numero_cifrado = pow(numero_original, e, N)
print(f"Número Cifrado (C): {numero_cifrado} <-- Esto se envía")
print("-" * 30)


# === PASO 4: DESCIFRADO ===
print("--- DESCIFRADO ---")
print(f"Recibimos C={numero_cifrado}, d={d}, N={N}")

# Fórmula de Descifrado: M = C^d mod N
numero_descifrado = pow(numero_cifrado, d, N)
print(f"Número Descifrado (calculado): {numero_descifrado}")

# Convertir el número de vuelta a caracter
mensaje_descifrado = chr(numero_descifrado)
print(f"Mensaje Descifrado: '{mensaje_descifrado}'")
print("-" * 30)

