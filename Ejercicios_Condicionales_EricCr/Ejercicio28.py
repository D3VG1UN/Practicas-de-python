#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.
letra=str(input("Introduce una letra: "))


if letra.islower():
    print("La letra es minúscula.")
elif letra.isupper():
    print("La letra es mayúscula.")
elif letra.isnumeric():
    print("El valor introducido es un número.")
elif not letra.isalpha() and not letra.isspace():
    print("El valor introducido un símbolo")
else:
    print("La letra es mayúscula ¿?")