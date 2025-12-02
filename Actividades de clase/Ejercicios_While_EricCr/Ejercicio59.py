#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random

azar=random.randint(1, 1000)
preguntar=1
intentos=0

while preguntar==1:
    num=int(input("Introduce un número entre 1 y 1000: "))
    

    if num<azar:
        print("El número que has introducido es menor que el aleatorio")
        intentos+=1
    elif num>azar:
        print("El número que has introducido es mayor que el aleatorio")
        intentos+=1
    else:
        print("Has acertado el número!")
        print(f"La cantidad de intentos ha sido de {intentos+1}")
        preguntar=0