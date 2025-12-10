#Programación de la segunda versión del proyecto password - criterio C.
print("INSTRUCCIONES:")
print("1. La longitud del password tiene que tener un mínimo de 8 caracteres.")
print("2. La contraseña tiene que contener los siguientes valores: ")
print("     Dos números mayores o iguales que 1 y menores o iguales que 5")
print("     Dos letras minúsculas")
print("     Una letra mayúscula")
print("     Dos de los siguientes símbolos *, _, @, &, /, #")
print("     Un número mayor o igual que 6 y menor o igual que 9")
#He eliminado la última condición, y he puesto dos valores >= 1 o <=5, porque me causaba problemas en el código
#Asimismo, he juntado un poco las condiciones para que las minúsculas, por ejemplo, no estén en líneas separadas
formatocorrecto=0
formatoincorrecto=0
for x in range (0, 3):
    password=input("Introduzca su contraseña: ")
    minusculas="qwertyuiopasdfghjklñzxcvbnm"
    mayusculas=minusculas.upper()

    nums_1_5=0
    minus=0
    mayus=0
    simbolos=0
    nums6_9=0
    incorrecto=0


    if len(password) < 8: 
        print("La longitud del password es incorrecta")
    else: 
        for i in range (len(password)):
            if password[i].isdigit():
                #Compruebo si es un dígito (es decir, un número) para no hacer int una letra
                if int(password[i]) >=1 and int(password[i]) <= 5:
                    nums_1_5+=1
                elif int(password[i]) >= 6 or int(password[i]) <=5:
                    nums6_9+=1
            #Con la variable ya establecida, con todas las letras minúsculas del teclado, hago la variable mayúscula
            #con .upper() y así puedo comprobarlo
            elif password[i] in minusculas:
                minus+=1
            elif password[i] in mayusculas:
                mayus+=1
            elif password[i] in ["*", "_", "@", "&", "/", "#"]:
            #Aquí utilizo una lista porque es más cómodo, en este caso, para la comprobación
                simbolos+=1
            else:
                
                print("Password incorrecto")
                incorrecto+=1

#Compruebo si todas las condiciones se cumplen y que no haya ningún en los dígitos.
    if nums_1_5 >= 2 and minus >= 2 and mayus >= 1 and simbolos >= 2 and nums6_9 >= 1 and incorrecto==0:
        print("Password correcto. Se cumplen las condiciones mínimas.")
        formatocorrecto+=1
    else:
        print("Password incorrecto. No se cumple alguna/s de las condiciones mínimas.")
        if formatoincorrecto < 3:
            formatoincorrecto+=1
        else:
            formatoincorrecto=formatoincorrecto

print(f"Ha introducido {formatocorrecto} passwords correctos y {formatoincorrecto} passwords incorrectos")

#Contraseñas de testeo:
#9Ip3C/* -------------------------------- Password incorrecto
#2cA_p7/ -------------------------------- Password incorrecto (longitud)
#3iO_m28/ ------------------------------- Password correcto
#99io*/55 ------------------------------- Password incorrecto
#4oLn8// -------------------------------- Password incorrecto
#23uoV*#9 ------------------------------- Password correcto
#/i4O94i/ ------------------------------- Password correcto
#3O7nl4//_ ------------------------------ Password correcto
#tI_73n_ -------------------------------- Password incorrecto (longitud incorrecta)
#z95Lp&1@ ------------------------------- Password correcto
