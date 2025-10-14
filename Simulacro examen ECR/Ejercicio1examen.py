nombre = input("Introduce tu nombre: ")
edad = int(input("Introdfuce tu edad: "))

nombre=nombre.upper()

if edad>0 and edad < 100:
    año_actual=2025
    futuro=año_actual + (100-edad)
    print(f"Hola {nombre}, cumplirás 100 años en el año {futuro}")
else: 
    print("Edad no válida")