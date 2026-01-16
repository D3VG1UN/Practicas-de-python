#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

lista1=[]
lista2=[]
x=int(input("Introduce cuántas palabras quieres en la lista: "))
palabra=""

for i in range (x):
    palabra=input("Introduce la palabra: ")
    lista1.append(palabra)
    lista2.append(palabra)

    

lista2.reverse()
print(f"lista1 contiene: {lista1}")
print(f"lista2 contiene: {lista2}")