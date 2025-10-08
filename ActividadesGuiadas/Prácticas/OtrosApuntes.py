#Se puede hacer una enumeración de variables, para ocupar menos lineas de codigo

#Por ejemplo:

var1,var2,var3="hello world",2,"19"

print(var1, var2, var3)

#Para usar los métodos string, la variable TIENE que ser un texto. Por lo tanto, debemos usar texto en vez de números.
#Si después necesitamos un número, podemos reasignar un estado de variable. Por ejemplo:
import math

diametro=input("Introduce el diametro: ")
if diametro.isnumeric() and int(diametro)>=1 and int(diametro)<=10:
    diametro=int(diametro)
    radio=diametro/2
    area=math.pi*radio**2
    perimetro=2*(math.pi*radio)
    print(round(area,2))

#Después de este código, añadimso código con operador lógico para comprobar si el número está entre 1 y 10
#                                            (and, or y not)