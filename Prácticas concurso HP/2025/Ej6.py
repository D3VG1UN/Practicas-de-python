notas=""
cantidadnotas=int(input("Cuántas notas? "))

for i in range (cantidadnotas):
    nota=float(input("Introduce la nota: "))
    dec=int(input("Introduce los decimales: "))
    nota=round(nota, dec)
    notas= str(nota) + ""
print(notas)