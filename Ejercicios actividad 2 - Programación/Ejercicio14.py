#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.

DiamCírculo=float(input("Introduce el diámetro del círculo: "))

import math
#La librería "math" te facilita cálculos más avanzados que los simples como 
#la multiplicación o la división gracias a nuevas funciones y constantes

RadioCírculo=DiamCírculo/2

Área=round(math.pi*(RadioCírculo**2), 1)
Perímetro=round(2*math.pi*RadioCírculo, 1)

print(f"El perímetro es: {Perímetro}")
print(f"El área es: {Área}")
