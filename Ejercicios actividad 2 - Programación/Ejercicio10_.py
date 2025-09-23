#Introduce por teclado dos números y muestre por pantalla la siguiente información: 
#cociente, resto y si el dividendo es par o impar. GIMP

div1=float(input("Introduce un número para la división: "))
div2=float(input("Introduce otro número para la división: "))

ResultDivisión=div1/div2
Resto=div1 % div2

print(f"El resultado de la división es de {ResultDivisión} y el resto es {Resto}")

if div1 % 2 == 0:
    print("El dividendo es un número par")
else:
    print ("El dividendo es un número impar")