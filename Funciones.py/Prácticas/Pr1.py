def sumar(num1, num2):
    suma=num1+num2
    print("La suma es:",suma)

def restar(num1, num2):
    resta=num1-num2
    print("La resta es:",resta)

def multiplicar(num1, num2):
    multiplicacion=num1*num2
    print("La multiplicación es:",multiplicacion)

def dividir(num1, num2):
    division=num1/num2
    print("La división es:",division)

sn=input("Sumar, restar, multiplicar o dividir, y qué 2 números (separa por espacios): ").lower()
lista_valores=sn.split(" ")
operacion=lista_valores[0]
numero1=int(lista_valores[1])
numero2=int(lista_valores[2])

if operacion=="sumar":
    sumar(numero1, numero2)
elif operacion=="restar":
    restar(numero1, numero2)
elif operacion=="multiplicar":
    multiplicar(numero1, numero2)
elif operacion=="dividir":
    dividir(numero1, numero2)
else:
    print("Haber introducido un valor correcto")