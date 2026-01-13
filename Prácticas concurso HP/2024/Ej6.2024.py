num=int(input("Introduce un numero: "))

resultado=0

for i in range (1, num+1):
    if (i%3==0):
        resultado=resultado+i

print(resultado)