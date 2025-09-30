#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo
import math

valorA=float(input("Introduce el valor de a para la ecuación: "))
valorB=float(input("Introduce el valor de b para la ecuación: "))
valorC=float(input("Introduce el valor de c para la ecuación: "))

Discriminante=valorB**2-4*valorA*valorC

if Discriminante > 0:
    x1=(-valorB+math.sqrt(Discriminante))/(2*valorA)
    x2=(-valorB-math.sqrt(Discriminante))/(2*valorA)
    print(f"El valor de x1 es {x1} y el valor de x2 es {x2}")
elif Discriminante == 0:
    x=-valorB/(2*valorA)
    print(f"Una solución real doble, x es igual a {x}")
else:
   print("La raíz no puede ser un número negativo")