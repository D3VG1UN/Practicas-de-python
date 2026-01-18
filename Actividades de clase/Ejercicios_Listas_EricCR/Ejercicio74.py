#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.

lista1=list(("casa","mesa","sal","sol","agua"))
lista2=list(("casa","luz","tres","tren","sol","pan"))
repetidos=[]
norepetidos=[]

for i in lista2:
    if i in lista1:
        repetidos.append(i)
    else:
        norepetidos.append(i)
for x in lista1:
    if x in lista2:
        if x not in repetidos:
            repetidos.append(x)
    else:
        norepetidos.append(x)

print(f"Repetidos: {repetidos}")
print(f"No repetidos: {norepetidos}")