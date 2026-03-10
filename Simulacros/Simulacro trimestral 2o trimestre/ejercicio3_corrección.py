listaproductos=[]
listaprecio=[]
listastock=[]
precio_total=0

lista=input("Introduce los valores: ").split("-")
for x in lista:
    lista2=x.split(":")
    listaproductos.append(lista2[0])
    listaprecio.append(lista2[1])
    listastock.append(lista2[2])

listaprecio=[int(i) for i in listaprecio]
listastock=[int(n) for n in listastock]

for j in range(len(listaprecio)):
    precio_total=precio_total+(listaprecio[j] * listastock[j])
print("El precio total es:",precio_total)

mascaro=max(listaprecio)
posicion=listaprecio.index(mascaro)
print("El producto más caro es:",listaproductos[posicion])

#stock 0
posicion=listastock.index(0)
print("EL producto con stock a cero es:",listaproductos[posicion])
listaprecio.pop(posicion)
listastock.pop(posicion)
listaproductos.pop(posicion)
print(listaproductos)