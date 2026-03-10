#Mostrar valores saltando número

inicio=int(input("Introduce el número de inicio: "))
fin=int(input("Introduce el número de fin: "))
incremento=int(input("Introduce el incremento: "))
iniciosuma=inicio
cuatro=0
repeticiones=int(fin/inicio)

for i in range (repeticiones):
    if i == 0:
        print(iniciosuma, end=",")
    else:
        iniciosuma=iniciosuma+incremento
        if iniciosuma % 4 == 0:
            cuatro=""
        elif iniciosuma % 6 == 0:
            if iniciosuma <= fin:
                print("*",iniciosuma,"*", end="," )
            else:
                print("*",iniciosuma,"*", end="")
        elif iniciosuma>=fin:
            repeticiones=0
        else:
            if iniciosuma <= fin:
                print(iniciosuma, end="," )
            else:
                print(iniciosuma, end="")

    
