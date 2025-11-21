#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 

#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%

#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")
pedidos=1
preciobocata1=9
preciobocata2=4.5
preciobocata3=2.5
preciocomplemento1=1.5
preciocomplemento2=1.75
preciocomplemento3=2
preciobebida1=2
preciobebida2=1.5
preciobebida3=1
total=0

while pedidos >= 1:
    bocadillo=int(input("Introduzca el bocadillo del menú que desea (1, 2 o 3): "))
    complemento=int(input("Introduzca el acompañamiento que desea (1, 2 o 3): "))
    bebida=int(input("Introduzca la bebida que desea tomar (1, 2 o 3): "))

    if bocadillo == 1:
        total=total+preciobocata1
    elif bocadillo == 2:
        total=total+preciobocata2
    elif bocadillo == 3:
        total=total+preciobocata3
    else:
        print("Por favor, introduzca un menú correcto")
        pedidos=0
    
    if complemento == 1:
        total=total+preciocomplemento1
    elif complemento == 2:
        total=total+preciocomplemento2
    elif complemento == 3:
        total=total+preciocomplemento3
    else:
        print("Por favor, introduzca un complemento correcto")
        pedidos=0
    
    if bebida == 1:
        total=total+preciobebida1
    elif bebida == 2:
        total=total+preciobebida2
    elif bebida == 3:
        total=total+preciobebida3
    else:
        print("Por favor, introduzca una bebida correcta")
        pedidos=0