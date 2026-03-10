productos=input().split("-")
separado=[]
producto=""
precio=""
stock=''
print(productos)

lista_producto = []
lista_precio = []
lista_stock = []

total=0
caro=0
productos_cero=[]
precio=0
precio_antiguo=0
turno=0

for i in range (len(productos)):
    separado=productos[i].split(":")
    for x in range(len(separado)):
        if producto==separado[0]:
            if precio==separado[1]:
                stock=separado[x]
            else:
                precio=separado[x]
        else:
            producto=separado[x]
    
    lista_producto.append(producto)
    lista_precio.append(precio)
    lista_stock.append(stock)

for x in range (len(lista_producto)):
    turno+=1
    if stock[i] == 0:
        productos_cero=producto[i] + " " + precio[i] + " " + stock[i]
        lista_stock.remove(stock[i])
        lista_producto.remove(producto[i])
        lista_precio.remove(precio[i])
    else:
        if turno==1:
            precio==int(precio[i])*int(stock[i])
            precio_antiguo=precio
            total+=int(precio[i])*int(stock[i])
        else:
            precio==int(precio[i])*int(stock[i])
            if precio>=precio_antiguo:
                caro=precio
            else:
                caro=precio_antiguo

print(lista_producto)
print(lista_precio)
print(lista_stock)