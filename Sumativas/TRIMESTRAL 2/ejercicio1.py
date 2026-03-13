nums=input("Introduce los números separados por un guion: ")
lista_nums=nums.split("-")

lista_num_int=[int(x) for x in lista_nums]
lista_final=lista_num_int

nummax=max(lista_num_int)
nummin=min(lista_num_int)
#antes usaba .sort(), después el índice 0 y el índice len(lista)-1, pero así es más comodo

promedio=round(sum(lista_num_int)/len(lista_num_int),4)

for i in (lista_num_int):
    if i<promedio:
        lista_final.remove(i)

for x in lista_num_int:
    if x < promedio:
        lista_final.remove(x)
#por algún motivo, con un solo for, se dejaba un número - he puesto otro for y se ha solucionado
print("Máximo:",nummax)
print("Mínimo:",nummin)
print("Promedio:",promedio)
print("Nueva lista:",lista_final)