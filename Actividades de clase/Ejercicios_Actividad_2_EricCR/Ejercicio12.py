# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

Lado=float(input("Introduce el valor del lado del trapecio isósceles: "))
BaseMenor=float(input("Introduce el valor de la base menor del trapecio: "))
BaseMayor=float(input("introduce el valor de la base mayor del trapecio: "))
Altura=float(input("Ahora introduce la altura del trapecio: "))

PerímetroTrapecio=BaseMenor+BaseMayor+(Lado*2)
ÁreaTrapecio=((BaseMenor+BaseMayor)/2)*Altura

print(f"El perímetro es: {PerímetroTrapecio}")
print(f"El área es: {ÁreaTrapecio}")