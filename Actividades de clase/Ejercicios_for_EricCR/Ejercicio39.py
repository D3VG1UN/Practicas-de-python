#Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

n=int(input("Introduce la cantidad de números introducidos: "))
totalpos=0
totalneg=0
total0=0

for i in range (n):
    num=float(input("Introduce un número: "))
    if num<0:
        totalneg=totalneg+1
    elif num == 0:
        total0=total0+1
    else:
        totalpos=totalpos+1
print(f"La cantidad de números positivos es: {totalpos}")
print(f"La cantidad de números negativos es: {totalneg}")
print(f"La cantidad de números ceros es: {total0}")