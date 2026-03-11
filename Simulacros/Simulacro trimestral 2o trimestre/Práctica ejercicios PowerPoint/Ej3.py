#Ejercicio 3: Uso de set() y eliminación de duplicados Escribe un programa que tome una lista de números 
#enteros (que puede contener elementos duplicados) y elimine los números repetidos. Utiliza la función set() 
#para resolverlo y luego convierte el conjunto de vuelta en una lista. Imprime la lista sin duplicados.

lista_nums=[3,4,654,5,6,3,3,4,5,6,4,3,2,5,6,7,7,85,7,575,7]

sin_reps=set(lista_nums)

lista_sin_reps=list(sin_reps)
sn=input("Quieres ver la lista con los números ordenados de mayor a menor? (s/n) ").lower()
if sn=="s":
    lista_sin_reps.sort()
    print(lista_sin_reps)
else:
    print(lista_sin_reps)