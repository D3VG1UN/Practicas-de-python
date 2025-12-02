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
    
    if num==2:
        dos+=1
    
    if num==3:
        tres+=1