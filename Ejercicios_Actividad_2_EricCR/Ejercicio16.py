# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).
import math

Número=float(input("Introduce un número para la raíz y la división: "))

RaízCuadrada=round(math.sqrt(Número), 1)
División=RaízCuadrada//2

print("La raíz cuadrada del número es:", RaízCuadrada)
print("La división del número es:", División)