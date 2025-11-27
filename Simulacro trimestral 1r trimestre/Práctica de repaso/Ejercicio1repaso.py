
concatenar=""
inicio=int(input("Introduce un número de inicio: "))
fin=int(input("Introduce un número de fin: "))
incremento=int(input("Introduce el incremento: "))

for i in range (inicio, fin, incremento):
    if not i%4==0:
        if i%6==0:
            concatenar=concatenar + "*" + str(i) + "*" + ","
        else:
            concatenar=concatenar + str(i) + ","
print(concatenar[:-1])