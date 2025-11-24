#Programación del proyecto password - criterio C.
print("INSTRUCCIONES:")
print("1. La longitud del password tiene que tener entre 6 y 8 caracteres.")
print("2. Forzar los siguientes valores según la posición indicada: ")
print("     Posición 1: Un número mayor o igual que 1 y menor o igual que 5")
print("     Posición 2: Una letra minúscula")
print("     Posición 3: Una letra mayúscula")
print("     Posición 4: Uno de los siguientes símbolos *, _, @")
print("     Posición 5: Una letra minúscula")
print("     Posición 6: Un número mayor o igual que 6 y menor o igual que 9")
print("     Posición 7: Uno de los siguientes símbolos &, /, #")
print("     Posición 8: Un número menor o igual que 5")
#Establecemos variables para luego cambiarlas si vemos que se cumplen o no las condiciones.
password=str(input("Introduce una palabra clave: "))
error0=error1=error2=error3=error4=error5=error6=error7=error8=0
lonpassword=len(password)

#utilizaré una serie de "ifs", en la que, si una condición no se cumple, 
#se cambie el valor de esa variable a lo que se mostrará por pantalla pero el programa siga.
if lonpassword>=6 and lonpassword<=8:
    error0=1
else:
    print(f"Error, el password tiene una longitud de {lonpassword} caracteres y no cumple los requisitos.")
#Ahora, con el error establecido a 1 si la contraseña es correcta, puedo seguir el código
if error0==1:
    if password[0]>="1" and password[0]<="5":
        error1=""
    else:
        error1="Error en el caracter 1"
if error0==1:
    if password[1].islower():
        error2=""
    else:
        error2="Error en el caracter 2"
if error0==1:
    if password[2].isupper():
        error3=""
    else:
        error3="Error en el caracter 3"
#he estado indagando un poco, ya que el código anterior me funcionaba incorrectamente, y he encontrado que la mejor
#solución es esta, utilizar "in"
if error0==1:
    if password[3] in ["*", "_", "@"]:
        error4=""
    else:
        error4="Error en el caracter 4"
if error0==1:
    if password[4].islower():
        error5=""
    else:
        error5="Error en el caracter 5"
if error0==1:
    if password[5]>="6" and password[5]<="9":
        error6=""
    else:
        error6="Error en el caracter 6"
if error0==1 and lonpassword>=7:
    if password[6] in ["&", "/", "#"]:
        error7=""
    else:
        error7="Error en el caracter 7"
else:
    error7=""
#en estos añado otro else, ya que, si la longitud es menor que 7, significa que tendrá 6 caracteres y, por tanto,
#no necesariamente estará mal. Lo mismo pasa en el 8.
if error0==1 and lonpassword==8:
    if password[7]<="5":
        error8=""
    else:
        error8="Error en el caracter 8"
else:
    error8=""
#ahora imprimo los valores por pantalla para que, en los que haya errores, se vea, y si no, se deje un espacio.
#además, hago una concatenación de "ands" ya que, si no hay ningún error, todas las variables tendrán ese valor.
if (error1=="" and error2=="" and error3=="" and error4=="" and error5=="" and error6=="" and error7=="" and error8==""):
    print("El formato del PASSWORD es válido")
else:
    print(error1,error2,error3,error4,error5,error6,error7,error8)