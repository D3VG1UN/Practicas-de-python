#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
#lista al azar.
import random

lista1=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
numrandom=0

for i in lista1:
    numrandom=random.randint(0,7)

print(lista1[numrandom])