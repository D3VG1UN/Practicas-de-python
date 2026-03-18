def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    area = ancho * alto
    return area
#return es opcional, pero se necesita para acceder a los valores más adelante

# Llamar a la función
resultado = calcular_area_rectangulo(5, 10)
print(resultado)  # Salida: 50

# El orden importa
resultado2 = calcular_area_rectangulo(10, 5)
print(resultado2)  # Salida: 50 (mismo resultado en este caso)