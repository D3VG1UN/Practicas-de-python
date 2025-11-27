#Comprobación de longitud y producto de cifras

producto=1
pares=0
cifras=int(input("Introduzca la cantidad de cifras: "))
num=(input("Introduce el número con esas cifras: "))

if len(num) == cifras:
    for i in range (cifras):
        producto=int(num[i])*producto
        if int(num[i]) % 2 == 0:
            pares+=1
        else:
            pares+=0
    print(f"El producto de las cifras es: {producto}")
    print(f"El total de cifras pares es: {pares}")
else:
    print("Longitud incorrecta")

