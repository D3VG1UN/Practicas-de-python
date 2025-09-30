#>,<,==,>=,<=,!=
#if condición1 operador condición2:
#!= significa "diferente de"
#en python, después de un "if", se añade una tabulación, donde se escribe el código

#Introducir un valor por teclado y que te diga si son iguales. Ejercicio de práctica.

var1=int(input("Introduce un valor: "))
var2=int(input("Introduce otro valor: "))
           
if var1 == var2:
    print("Las dos variables son iguales")
else:
    print("Las dos variables son diferentes")

#Crear un menú que te deje escoger entre las siguientes opciones:

Escogencia=int(input("Escoge un plato en el siguiente menú (introduce el número): "))
print("1. hamburguesa")
print("2. pizza")
print("3. lentejas")
print("4. bocadillo de jamón")

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