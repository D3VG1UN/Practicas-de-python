#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math

RadioCilindro=float(input("Introduce el valor del radio: "))
AlturaCilindro=float(input("Introduce el valor de la altura: "))

ÁreaCilindro=round(2*math.pi*RadioCilindro*(AlturaCilindro+RadioCilindro), 2)
VolumenCilindro=round(math.pi*(RadioCilindro**2)*AlturaCilindro, 2)

print(f"El área del cilindro es: {ÁreaCilindro} y el volumen es: {VolumenCilindro}")