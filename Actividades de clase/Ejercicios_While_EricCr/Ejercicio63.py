#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
import random
tiradas=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0

while tiradas<100:
    num=random.randint(1, 6)
    if num==1:
        uno+=1
        tiradas+=1
    elif num==2:
        dos+=1
        tiradas+=1
    elif num==3:
        tres+=1
        tiradas+=1
    elif num==4:
        cuatro+=1
        tiradas+=1
    elif num==5:
        cinco+=1
        tiradas+=1
    else:
        seis+=1
        tiradas+=1

print(f"Uno: {uno}")
print(f"Dos: {dos}")
print(f"Tres: {tres}")
print(f"Cuatro: {cuatro}")
print(f"Cinco: {cinco}")
print(f"Seis: {seis}")

