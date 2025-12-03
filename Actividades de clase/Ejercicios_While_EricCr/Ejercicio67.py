#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes 
#consideraciones:
print("CONSIDERACIONES:")
print("Debe tener una longitud entre 6 y 8 caracteres.")
print("Debe contener como mínimo:")
print("2 números mayores o iguales que 1 y menor o igual que 5")
print("2 letras minúsculas")
print("1 letra mayúscula")
print("2 símbolos (*, _, @, &,/,#)")
print("1 número mayor o igual que 6 y menor o igual que 5")

password=input("Introduzca su contraseña: ")
mensaje=""
correcto=1

if len(password)>8 or len(password) < 6: 
    print("La longitud del password es incorrecta")
else: 
    for i in range (len(password)):
        if int(password[i]) >=1 and int(password[i]) <= 5:
            correcto+=1