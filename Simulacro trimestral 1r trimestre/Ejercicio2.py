#Contar positivos, negativos y números mayores que 100

totalpositivos=0
totalnegativos=0
mayores100=0

for i in range (0, 7):
    num=int(input("Introduce un número: "))
    if num < 0:
        totalnegativos=totalnegativos+num
    elif num >=100:
        mayores100=mayores100+1
        num=num
    
    if num >= 0:
        totalpositivos=totalpositivos+num
    else:
        relleno=""


print(f"Suma positivos: {totalpositivos}")
print(f"Suma negativos: {totalnegativos}")
print(f"Mayores de 100: {mayores100}")