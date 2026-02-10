#ejercicio 7. máximo de tres iguales

num=input()
if " " in num:
    listanum=num.split()
    maximo=max(int(listanum[0]), int(listanum[1]), int(listanum[2]))
    print(maximo)