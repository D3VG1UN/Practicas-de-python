#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?
import random

lista1=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
listapuntos=[]
numrandom=random.randint(0,7)
respuesta=lista1[numrandom]
intento=""
partidas=int(input("Cuántas partidas quieres jugar?: "))
puntosrecibir=8
puntosrecibirigual=8

for i in range(partidas):
    puntosrecibir=puntosrecibirigual
    print(f"Las opciones son: {lista1}")

    while intento!=respuesta and puntosrecibir>0:
        intento=input("Intenta adivinar la palabra: ")

        if intento==respuesta:
            print("ACERTASTE")
            listapuntos.append(puntosrecibir)
        else:
            puntosrecibir-=1
            print("SIGUE JUGANDO")

    intento=""  

print("Tus puntuaciones son:", listapuntos)

total=sum(listapuntos)
media=(partidas*8)/2

print(f"Puntuación total: {total}")
print(f"La media para tener buena suerte era: {media}")

if total>media:
    print("La suerte te acompaña")
else:
    print("Mejor no te dediques a los juegos de azar")
