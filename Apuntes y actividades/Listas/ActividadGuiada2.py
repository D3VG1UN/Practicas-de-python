#Ejercicio 2 - introducir números separados por guiones, distinguir numericos de textuales y enseñar en una lista
#versión con "for x in"
import string
listanumeros=[]
listanonumeros=[]
listatodo=[]

frase=input("Introduce valores separados por un guion: ")

listatodo=frase.split("-")

for x in listatodo:
    if x.isnumeric():
        listanumeros.append(int(x))
    else:
        listanonumeros.append(x)

print(listanumeros)
print(listanonumeros)
print(sum(listanumeros))