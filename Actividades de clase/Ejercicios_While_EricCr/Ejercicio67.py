#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes 
#consideraciones:
print("CONSIDERACIONES PARA ESTABLECER SU CONTRASEÑA:")
print("Debe tener una longitud entre 6 y 8 caracteres.")
print("Debe contener como mínimo:")
print("2 números mayores o iguales que 1 y menor o igual que 5")
print("2 letras minúsculas")
print("1 letra mayúscula")
print("2 símbolos (*, _, @, &,/,#)")
print("1 número mayor o igual que 6 y menor o igual que 9")

password=input("Introduzca su contraseña: ")
mensaje=""
minusculas="qwertyuiopasdfghjklñzxcvbnm"
mayusculas=minusculas.upper()

nums_1_5=0
minus=0
mayus=0
simbolos=0
nums6_9=0


if len(password)>8 or len(password) < 6: 
    print("La longitud del password es incorrecta")
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
if nums_1_5 >= 2 and minus >= 2 and mayus >= 1 and simbolos >= 2 and nums6_9 >= 1:
    print("Password correcta")
else:
    print("Password incorrecto")
        
        