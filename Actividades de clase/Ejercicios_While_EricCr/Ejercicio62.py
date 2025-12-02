#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
pares=""
impares=""

if num1<num2:
    for i in range (num1, num2, 1):
        if num1%2==0:
            pares=pares + str(num1) + "-"
            num1+=1
        else:
            impares=impares + str(num1) + "-"
            num1+=1
    print(pares[:-1])
    print(impares[:-1])

if num1>num2:
    for j in range (num1, num2, -1):
        if num2%2==0:
            pares=pares + str(num2) + "-"
            num2+=1
        else:
            impares=impares + str(num2) + "-"
            num2+=1
    print(pares[:-1])
    print(impares[:-1])

