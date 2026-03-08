productos = input().split("-")

lista_producto = []
lista_precio = []
lista_stock = []

total = 0
caro = 0
producto_caro = ""
productos_cero = []

# Separar datos
for i in range(len(productos)):
    separado = productos[i].split(":")
    
    producto = separado[0]
    precio = int(separado[1])
    stock = int(separado[2])

    lista_producto.append(producto)
    lista_precio.append(precio)
    lista_stock.append(stock)

# Calcular valores
for i in range(len(lista_producto)):
    
    if lista_stock[i] == 0:
        productos_cero.append(lista_producto[i])
    else:
        valor = lista_precio[i] * lista_stock[i]
        total += valor

        if lista_precio[i] > caro:
            caro = lista_precio[i]
            producto_caro = lista_producto[i]

# Eliminar productos con stock 0
i = 0
while i < len(lista_stock):
    if lista_stock[i] == 0:
        lista_stock.pop(i)
        lista_precio.pop(i)
        lista_producto.pop(i)
    else:
        i += 1

# Resultados
print("Valor total del inventario:", total)
print("Producto más caro:", producto_caro, "-", caro)
print("Productos con stock 0:", productos_cero)

print("Resumen final:")
for i in range(len(lista_producto)):
    print(lista_producto[i], lista_precio[i], lista_stock[i])