#Programa para escoger uno de los menús para repostar el vehiculo
#Primero usamos print para enseñar las opciones
print("****GASOLINERA****")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
print("*******************")
#Y luego pedimos el tipo y los litros a repostar.
opcion=int(input("Escoja el tipo de combustible deseado: "))
litros=float(input("Introduzca el número de litros a repostar: "))

#Ahora que tenemos los datos podemos calcular el precio, y si es necesario, con descuento, dependiendo del menú. 
#Utilizamos if y elif para comprobar qué menú ha escogido
if opcion == 1:
    pagar1=round(litros*1.765, 2)
    print("El total a pagar es: ",pagar1)
elif opcion == 2:
    pagar2=round(litros*1.913, 2)
    descuento2=(10*pagar2)/100
    pagardescuento2=round(pagar2-descuento2, 2)
    print(f"El total a pagar es: {pagar2} y con el descuento queda en: {pagardescuento2}")
elif opcion == 3:
    pagar3=round(litros*1.746, 2)
    print("El total a pagar es: ",pagar3)
elif opcion == 4:
    pagar4=round(litros*1.839, 2)
    descuento4=(12*pagar4)/100
    pagardescuento4=round(pagar4-descuento4, 2)
    print(f"El total a pagar es: {pagar4} y con el descuento queda en: {pagardescuento4}")
else:
    print("Por favor, introduzca uno de los menús disponibles")
#Añadimos un else al final por si se da el caso que el usuario selecciona un menú incorrecto.