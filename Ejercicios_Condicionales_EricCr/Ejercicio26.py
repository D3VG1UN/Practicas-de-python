#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

letra=str(input("Introduce una letra: "))

#Con los métodos string podemos comprobar y trnasformar palabras.
if letra.islower()==True:
    print("La letra es minúscula.")
elif letra.isupper()==True:
    print("La letra es mayúscula.")
else:
    print("La letra es mayúscula ¿?")