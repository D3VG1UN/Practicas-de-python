#Programa que sume los n primeros números naturales. n Lo introduce el usuario.

total=0
numNaturales=1
n=int(input("Introduce la cantidad de números que quieres sumar: "))

for i in range (n+1):
    total=total+i
print(total)