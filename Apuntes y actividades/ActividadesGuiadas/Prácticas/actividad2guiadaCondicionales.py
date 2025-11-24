#>,<,==,>=,<=,!=
#if condición1 operador condición2:
#!= significa "diferente de"
#en python, después de un "if", se añade una tabulación, donde se escribe el código

#Introducir un valor por teclado y que te diga si son iguales. Ejercicio de práctica.
#Se pueden introducir las palabras and, or y not para poner más de una variable

#Por ejemplo: if var==2 or var==4:
#O: if var==3 and var1==6:
#if not op==op1:

var1=int(input("Introduce un valor: "))
var2=int(input("Introduce otro valor: "))
           
if var1 == var2:
    print("Las dos variables son iguales")
else:
    print("Las dos variables son diferentes")
