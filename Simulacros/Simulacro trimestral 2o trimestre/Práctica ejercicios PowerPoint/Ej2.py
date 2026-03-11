#Ejercicio 2: Manipulación de cadenas con listas Escribe un programa que pida al usuario una cadena de texto 
#y la convierta en una lista de palabras. Luego, realiza lo siguiente:
#•Imprime la lista de palabras.
#•Cuenta cuántas veces aparece una palabra específica (la que elija el usuario).
#•Une la lista de palabras nuevamente en una cadena de texto separada por espacios.

palabras=input("Introduzca cadena de palabras: ")
lista_palabras=palabras.split("-")

print(lista_palabras)

palabraes=input("Qué palabra quieres buscar: ")
veces=lista_palabras.count(palabraes)
if veces>1:
    print("Sale",veces,"veces")
elif veces==1:
    print("Sale",veces,"vez")
else:
    print("No está")

palabrasEspacio=" ".join(lista_palabras)
print(palabrasEspacio)