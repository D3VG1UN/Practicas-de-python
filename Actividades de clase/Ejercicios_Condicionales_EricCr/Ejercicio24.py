#Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
#Qué tenía mal:
#1. La variable no está bien definida, no debe empezar por un número. Por tanto, el resto de esas variables
#en el ejercicio estaban mal definidas también
#2. falta un float antes del input de la var2
#3. La variable "var_imc" está usando el ==, que sirve para comprobar si algo es igual a algo. Como queremos
#asignar un valor, usamos simplemente =
#4. En el comentario, hemos puesto mal las variables. Al estar entre llaver, se tiene que poner una f antes de las
#comillas, para que funcione
#5. La variable está mal definida, ya que no empieza con mayúscula, sino con minúscula.
#6. Al final del "if" se debe poner siempre :
#7. Después de un if, debajo, lo que quieres que se cumpla, se debe poner con un tabulador. Lo mismo aplica para 
#el else.

var1=float(input("Introduce el peso: "))
var2=float(input("Introduce la altura: "))
var_imc=var1 / var2**2
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es:", 
var_imc)
if var_imc>25:
    print("Hay sobrepeso")
else:
    print("Estás dentro de los parámetros normales")