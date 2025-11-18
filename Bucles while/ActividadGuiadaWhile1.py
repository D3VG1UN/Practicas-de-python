#Adivina el número
import random

num_secreto=random.randint(1, 20)
numero=int(input("Introduce un número del 1 al 20: "))

while num_secreto!=numero or (numero<0 and numero>20):
    print(f"has introducido el numero {numero}, no has acertado")
    numero=int(input("Vuelve a introducir un valor: "))

print("acertaste")
