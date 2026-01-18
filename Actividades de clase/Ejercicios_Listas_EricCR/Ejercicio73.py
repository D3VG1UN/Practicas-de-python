#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no

lista1=list(("casa","mesa","sal","sol","agua"))
lista2=list(("casa","luz","tres","tren","sol","pan"))
repetidos=[]
norepetidos=[]

for i in lista2:
    if i in lista1:
        repetidos.append(i)
    else:
        norepetidos.append(i)

print(f"Repetidos: {repetidos}")
print(f"No repetidos: {norepetidos}")