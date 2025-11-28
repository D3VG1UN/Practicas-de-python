#Modificar un valor total con reglas distintas
valor=100
repetir=1

while repetir==1:
    numero=int(input("Introduce un número: "))

    if numero%2==0:
        valor=valor/2

    if numero%2!=0:
        valor+=numero
        if numero%3==0:
            valor-=5
    
    if numero<0:
        print("Número introducido es negativo. Final")
        repetir=0

    elif valor<50:
        print(int(valor))
        print("Final")
        repetir=0
    
    elif valor>150:
        print(int(valor))
        print("Final")
        repetir=0
    
    else:
        print(int(valor))
        print("Continúa")
        repetir=1