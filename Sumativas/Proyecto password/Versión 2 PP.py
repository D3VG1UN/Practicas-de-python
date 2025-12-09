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


    if len(password)>8 or len(password) < 6: 
        print("La longitud del password es incorrecta")
        formatoincorrecto+=1
    else: 
        for i in range (len(password)):
            if password[i].isdigit():
                #Compruebo si es un dígito (es decir, un número) para no hacer int una letra
                if int(password[i]) >=1 and int(password[i]) <= 5:
                    nums_1_5+=1
                elif int(password[i]) >= 6 or int(password[i]) <=5:
                    nums6_9+=1
            elif password[i] in minusculas:
                minus+=1
            elif password[i] in mayusculas:
                mayus+=1
            elif password[i] in ["*", "_", "@", "&", "/", "#"]:
            #Aquí utilizo una lista porque es más cómodo, en este caso, para la comprobación
                simbolos+=1
            else:
                print("Pasword incorrecto")

#Compruebo si todas las condiciones se cumplen.
    if len(password) == 8:
        if nums_1_5 >= 2 and minus >= 2 and mayus >= 1 and simbolos >= 2 and nums6_9 >= 1:
            print("Password correcto")
            formatocorrecto+=1
        else:
            print("Password incorrecto")
            if formatoincorrecto < 3:
                formatoincorrecto+=1
            else:
                formatoincorrecto=formatoincorrecto

print(f"Ha introducido {formatocorrecto} passwords correctos y {formatoincorrecto} passwords incorrectos")

#Contraseñas de testeo:
#9Ip3C/* -------------------------------- Password incorrecto
#2cA_p7/