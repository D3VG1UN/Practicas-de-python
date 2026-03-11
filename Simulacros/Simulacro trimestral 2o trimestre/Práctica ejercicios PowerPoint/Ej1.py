#Ejercicio 1: Operaciones con listas Crea una lista de números enteros. Escribe un programa que realice las 
#siguientes operaciones:
#•Encuentra el número máximo y mínimo de la lista.
#•Calcula la suma de todos los elementos de la lista.
#•Crea una nueva lista con los elementos de la lista original multiplicados por 2

lista_inicial=[2,6,78,3,254,53,10]

nummax=max(lista_inicial)
nummin=min(lista_inicial)

sumatotal=sum(lista_inicial)

lista_nueva=[x*2 for x in lista_inicial]

print("El número máximo es:",nummax)
print("El número mínimo es:",nummin)
print("")
print("La suma de todos los elementos de la lista es:",sumatotal)
print("Y la nueva lista con todos los números multiplicados por 2 es:",lista_nueva)