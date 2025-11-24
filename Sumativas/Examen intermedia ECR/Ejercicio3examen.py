#Calculamos el área de un triángulo equilátero en base a uno de los lados
import math
#Importamos la librería math para cuando necesitemos la raíz cuadrada, y esta función sólo se puede usar con esta librería.

valora=float(input("Introduce el valor de a: "))

area=round((math.sqrt(3)/4)*valora**2, 2)
#Usamos la fórmula con sqrt. de la librería math para calcular la raíz cuadrada.
#sqrt significa "SQuare RooT", "raíz cuadrada" en inglés

print(f"El área del triángulo con un lado {valora} es: ",area)