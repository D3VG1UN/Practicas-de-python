#Crea un programa que cuente todos los números pares hasta el número 50

pares=0
impares=0

for i in range(50):
    if pares==impares:
        pares=pares+1
    else:
        impares=impares+1

print(f"El total de pares es: {pares}")
print(f"El total de impares es: {impares}")