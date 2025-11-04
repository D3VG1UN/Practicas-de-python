#Programa que al introducir un número por teclado permita mostrar ese número de veces tu 
#nombre

nombre=input("Introduce tu nombre: ")
num=int(input("Introduce la cantidad d eveces que quieres que tu nombre aparezca por pantalla: "))

for num in range(num):
    print(nombre)