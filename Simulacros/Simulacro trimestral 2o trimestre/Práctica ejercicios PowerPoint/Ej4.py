#Ejercicio 4: Diseña un programa donde el usuario introduzca todos los valores en una línea separados por 
#un guion. Separa los valores que sean numéricos de los que no utilizando listas. Suma los valores 
#numéricos para obtener el total.

valores=input("Introduce los valores con guion: ")
lista_valores=valores.split("-")

numericos=[]
nonumericos=[]

for i in lista_valores:
    if i.isnumeric():
        numericos.append(i)
    else:
        nonumericos.append(i)
print(numericos,nonumericos)

numericos_int=[int(x) for x in numericos]
total=sum(numericos_int)

print(total)