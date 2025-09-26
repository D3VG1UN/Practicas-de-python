#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10

num1=int(input("Introduce el primer número entre 1 y 10: "))
num2=int(input("Introduce el segundo número entre 1 y 10: "))

#Puedo hacer estas comparaciones seguidas para establecer un límite.
#Después utilizo el mismo código, aunque he tenido que moverlo todo hacia la derecha con el tab.
if 1 <= num1 <= 10 and 1 <= num2 <= 10:
    if num1 > num2:
        print(f"El número {num1} es mayor que el número {num2}")
    else:
        if num2 > num1:
            print(f"El número {num2} es mayor que el número {num1}")
        else:
            print(f"El número {num1} y el número {num2} son iguales")
else:
    print("Uno o los dos números están fuera de los límites establecidos")