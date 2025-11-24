#Revisar y corregir código.

#Algunos de los errores son: el nombre de la variable no puede tener espacios, falta específicar el tipo si es decimal, y faltan
#comillas dentro del input, y que es mejor que la variable no empiece por mayúscula
var1=float(input("Introduce el primer número: "))
var2=float(input("Introduce el segudo número: "))

vartotal=var1 + var2

#utilizando f no se pone una coma detrás, y las variables se ponen entre {}, también falta establecer correctamente las variables
#por su nombre
print(f"el resultado de sumar {var1} y {var2} es: ",vartotal)