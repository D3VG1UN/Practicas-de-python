#for
#el for se utiliza cuando sabemos el número de vecesque se tiene que repetir
#for j in range (0,10):
#for j in range (0,10,2):
#for j in string:

password="a7e4jkE"
vocales="aeiouAEIOU"

total=0
totalvocales=0
#repeticiones=int(input("Número de veces: "))
for i in password:
    if i.isnumeric():
        total=total+int(i)
#Comprobamos si la letra que se comprueba con el bucle está dentro del límite de vocales
    if i in vocales:
        totalvocales=totalvocales+1
print(total)
print(totalvocales)


#suma total de los numeros
#número de vocales













#while + condición
#se utiliza cuando el número de vueltas está indeterminado/que dependa del usuario, si quiere salir del bucle o no