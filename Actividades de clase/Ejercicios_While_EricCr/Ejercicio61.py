#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.

tabla=1
num=int(input("Introduce el número del que quieras saber la tabla: "))
multiplicar=0

while tabla <= 10:
    multiplicar=num*tabla
    if multiplicar < 40:
        print(multiplicar)
        tabla+=1
    else:
        print(multiplicar)
        print("Fin del programa")
        tabla=111111111111
    