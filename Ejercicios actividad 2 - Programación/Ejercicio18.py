# Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.

Niños=float(input("Introduce cuántos niños menores de 18 años asisten: "))
Adultos=float(input("Ahora introduce la cantidad de adultos que asisten: "))

RebajaNiños=(50/100)*12
PrecioNiños=12-RebajaNiños
PrecioMenores=round(PrecioNiños*Niños, 1)

RebajaAdultos=(10/100)*12
PrecioAdultos=12-RebajaAdultos
PrecioFinalA=round(PrecioAdultos*Adultos, 1)

Total=PrecioFinalA+PrecioMenores

print("El total a pagar del/los menor/es es de:", PrecioMenores)
print("El total a pagar del/los adulto/s es de:", PrecioFinalA)
print("El total a pagar es:", Total)