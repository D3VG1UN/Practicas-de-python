#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 
import string

num=list(input("Introduce un número "))
punt=".,"
decimal=1
letra=""

for x in num:
    if x in punt:
        decimal=1
    elif x.isalpha():
        letra="Si"
    else:
        decimal=0

if decimal==1 and not letra=="Si":
    print("El número es decimal")
if decimal==0:
    print("No es un número decimal")

#No sé como hacerlo y no encuentro el error