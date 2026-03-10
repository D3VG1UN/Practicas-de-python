#Modificar un valor total con reglas distintas

valor=100
repetir=1

while repetir == 1:
    numero=int(input("Introduce un número para el valor: "))
    if numero % 2 == 0:
        valor=int(valor/2)
    
    if numero % 2 != 0:
        valor=int(valor+numero)
    
    if numero % 3 == 0:
        valor=int(valor-5)
    
    if numero < 0:
        print("Fin del programa, el valor introducido es negativo")
        print(valor)
        repetir=0
    elif valor < 50:
        print(valor)
        print("Fin del programa, el valor es menor que 50")
        repetir=0
    elif valor > 150:
        print(valor)
        print("Fin del programa, el valor es mayor que 150")
        repetir=0
    else:
        print(valor)
        repetir=1