#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales

num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))

#Puedo introducir condicionales dentro de los condicionales, pero tienen que estar separados por tabs.
#Son como capas, cada tab añade una capa y en cada capa puede haber un condicional.
if num1 > num2:
    print(f"El número {num1} es mayor que el número {num2}")
else:
    if num2 > num1:
        print(f"El número {num2} es mayor que el número {num1}")
    else:
        print(f"El número {num1} y el número {num2} son iguales")
