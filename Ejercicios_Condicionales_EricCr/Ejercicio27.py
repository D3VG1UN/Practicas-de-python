#Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla.

letra=str(input("Introduce una letra: "))

#El True es innecesario, ya que el programa asume sin que se lo diga que el valor es cierto.
if letra.islower()==True:
    print("La letra es minúscula.")
elif letra.isupper()==True:
    print("La letra es mayúscula.")
elif letra.isnumeric()==True:
    print("El valor introducido es un número.")
else:
    print("La letra es mayúscula ¿?")