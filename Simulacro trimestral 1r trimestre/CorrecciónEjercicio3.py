multiplicar=1
contadorpares=0
cifras=int(input("Introduce las cifras: "))
numero=int(input("Introduce un número: "))
longitudnumero=len(str(numero))

if longitudnumero==cifras:
    for i in str(numero):
        multiplicar=multiplicar*int(i)
        if int(i)%2==0:
            contadorpares+=1
else:
    print("Longitud incorrecta")

print("Producto de cifras:",multiplicar)
print("Cifras pares:",contadorpares)