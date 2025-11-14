# Solicitar palabra al usuario
palabra = input("Introduce una palabra: ")

# Solicitar letra a buscar
letra = input("Introduce la letra a buscar: ")

# Buscar posiciones de la letra
posiciones = []
for i in range(len(palabra)):
    if palabra[i].lower() == letra.lower():
        posiciones.append(i)

# Mostrar resultados
if posiciones:
    print(f"La letra '{letra}' se encuentra en la palabra.")
    print(f"Aparece en las posiciones: {posiciones}")
    print(f"Total de apariciones: {len(posiciones)}")
else:
    print(f"La letra '{letra}' no se encuentra en la palabra.")