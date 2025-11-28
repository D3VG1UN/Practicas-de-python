#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random

numerorandom=random.randint(1, 5)
repetir=1

while repetir==1:
    num=int(input("Introduce un número entre 1 y 5: "))
    if num>0 and num<=5:
        if numerorandom==num:
            print("Numero acertado")
            repetir=0
        else:
            print("Numero no acertado")
            repetir=1
    else:
        print("Introduce un número correctamente entre 1 y 5")
        repetir=1