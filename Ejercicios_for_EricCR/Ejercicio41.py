#Imprime el siguiente patrón utilizando for

#Este ejercicio lo he hecho con la explicación de Miguel Angel, que, aunque no lo he entendido completamente
#Sé más o menos cómo hacerlo.
for i in range (5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print("")