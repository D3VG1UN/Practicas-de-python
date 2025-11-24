#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso

Peso=float(input("Introduzca se peso para el IMC: "))
Estatura=float(input("Ahora introduzca su altura en metros: "))

EstaturaIMC=Estatura**2
ÍndiceMasaCorporal=round(Peso/EstaturaIMC, 2)

if ÍndiceMasaCorporal >= 25:
    print(f"Si su peso es {Peso} y su altura es {Estatura}. su IMC es de {ÍndiceMasaCorporal}")
    print("Lamento decirle que usted tiene sobrepeso")
else:
    print(f"Si su peso es {Peso} y su altura es {Estatura}. su IMC es de {ÍndiceMasaCorporal}")