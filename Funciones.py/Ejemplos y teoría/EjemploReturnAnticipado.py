def es_par(numero):
    """Verifica si un número es par"""
    if numero % 2 == 0:
        return True  # Sale aquí si es par
    return False  # Solo se ejecuta si no es par

print(es_par(4))   # True
print(es_par(7))   # False