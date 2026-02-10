#ejercicio 5. máximo

num=input()
if " " in num:
    listanum=num.split()
    maximo=max(int(listanum[0]), int(listanum[1]))
    print(maximo)