#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while

tabla=1
num=int(input("Introduce el número del que quieras saber la tabla: "))
multiplicar=0

while tabla <= 10:
    multiplicar=num*tabla
    print(multiplicar)
    tabla+=1