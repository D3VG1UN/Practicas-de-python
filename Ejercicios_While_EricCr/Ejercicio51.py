#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While
veces=int(input("Introduce la cantidad de veces que salga Buenos días por pantalla: "))

while veces>0:
    print("Buenos días")
    veces=veces-1
