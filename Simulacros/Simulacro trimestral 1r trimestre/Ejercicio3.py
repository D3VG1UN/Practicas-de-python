#Comprobación de longitud y producto de cifras

cifras=int(input("Introduzca las cifras del número: "))
num=(input("Introduzca un número: "))
producto=1
pares=0


if len(num) == cifras:
    num=int(num)
    for i in range(num):
        if num[i] % 2==0:
            pares=pares+1
        else:
            pares=pares
        producto=producto*num[i]
else:
    print("Longitud incorrecta")