import math

radio=float(input("Introduce el radio del cilindro: "))
altura=float(input("Introduce la altura del cilindro: "))
formato=input("¿Qué formato de frase prefieres, minúsculas o mayúsculas? ")

volumen=math.pi*radio**2*altura
frase=str(f"El volumen del cilindro es:")

if formato == "mayúsculas":
    frasemayus=frase.upper()
    print(frasemayus,volumen)
elif formato == "minúsculas":
    fraseminus=frase.lower()
    print(fraseminus,volumen)
elif not formato=="mayúsculas" or not formato=="minúsculas":
    print("Introduce un formato válido o escribe correctamente el formato")