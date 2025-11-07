#Imprime el siguiente patrón utilizando for

num=54321
for i in range (5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print("")