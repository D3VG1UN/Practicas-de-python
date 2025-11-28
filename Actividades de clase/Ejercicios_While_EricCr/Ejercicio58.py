#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random

numerorandom=random.randint(1, 5)
intentos=3


while intentos>0:
    num=int(input("Introduce un número entre 1 y 5: "))
    if num>0 and num<=5:
        if numerorandom==num:
            print("Numero acertado")
            intentos=0
        else:
            print("Numero no acertado")
            intentos-=1
            print(f"Te quedan {intentos} intentos")
    else:
        print("Introduce un número correctamente entre 1 y 5")
        intentos-=1
        print(f"Te quedan {intentos} intentos")