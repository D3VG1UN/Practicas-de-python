#ejercicio 13. comparación

nombres=input()
if " " in nombres:
    listanombres=nombres.split()

a=listanombres[0]
b=listanombres[1]

if a > b:
    print(listanombres[0], ">", listanombres[1])
elif a < b:
    print(listanombres[0], "<", listanombres[1])
else:
    print(listanombres[0], "=", listanombres[1])
    