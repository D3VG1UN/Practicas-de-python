#Crear un menú que te deje escoger entre las siguientes opciones:
#Algo parecido entrará en el examen

print("1. hamburguesa")
print("2. pizza")
print("3. lentejas")
print("4. bocadillo de jamón")
Escogencia=int(input("Escoge un plato del menú (introduce el número): "))


if Escogencia == 1:
    print("Te serviremos una hamburguesa")
elif Escogencia == 2:
    print("Te serviremos una pizza")
elif Escogencia == 3:
    print("Te serviremos unas lentejas")
elif Escogencia == 4:
    print("te traeremos un bocadillo de jamón")
else:
    print("Creo que se ha equivocado de plato. Por favor, vuelva a pedir")

#Otra manera: if Escogencia>4 or Escogencia<1
#               print("Error")