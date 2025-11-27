#contar positivos, negativos y números mayores que 100
positivos=0
negativos=0
mayores100=0

for i in range (0, 7):
    num=int(input("Introduzca un número: "))

    if num < 0:
        negativos=negativos+num
        
    if num>0:
        positivos=positivos+num
        if num > 100:
            mayores100+=1

print("Suma positivos:",positivos)
print("Suma negativos:",negativos)
print("Mayores de 100:",mayores100)