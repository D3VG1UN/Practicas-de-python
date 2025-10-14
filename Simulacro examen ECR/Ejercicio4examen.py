print("Opción | Tarifa | Precio €/kWh | Descuento")
print("1 | Tarifa Nocturna | 0.158 | 5%")
print("2 | Tarifa Plana | 0.192 | 0%")
print("3 | Tarifa Solar | 0.143 | 8%")
print("4 | Tarifa Ecológica | 0.170 | 10%")

opcion=int(input("Selecciona una opción: "))
kWh=float(input("Introduce los kWh deseados: "))

if opcion == 1:
    precio1 = kWh*0.158
    descuento1 = (5*precio1)/100
    preciodescuento1 = precio1-descuento1
    print("El total a pagar es:",precio1)
    print("Con el descuento aplicado queda en:",preciodescuento1)
elif opcion == 2:
    precio2 = kWh*0.192
    preciodescuento2 = precio2
    print("El total a pagar es:",precio2)
    print("Con el descuento aplicado queda en:",preciodescuento2)
elif opcion == 3:
    precio3 = kWh*0.143
    descuento3 = (8*precio3)/100
    preciodescuento3 = precio3-descuento3
    print("El total a pagar es:",precio3)
    print("Con el descuento aplicado queda en:",preciodescuento3)
elif opcion == 4:
    precio4 = kWh*0.170
    descuento4 = (10*precio4)/100
    preciodescuento4 = precio4-descuento4
    print("El total a pagar es:",precio4)
    print("Con el descuento aplicado queda en:",preciodescuento4)
else: 
    print("Opción no válida")