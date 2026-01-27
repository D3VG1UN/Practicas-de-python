#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
import random

lista1=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
numrandom=random.randint(0,7)
respuesta=lista1[numrandom]
intento=""

while intento != respuesta:
    print(f"Las opciones son: {lista1}")
    intento=input("Intenta adivinar la palabra: ")
    if intento==respuesta:
        print("ACERTASTE")
    else:
        print("SIGUE JUGANDO")
    