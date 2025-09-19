#programa que te pida dos números, y que te de el resultado de una suma, resta, 
#multiplicación y división, y después buscar en internet los otros 3 
#operadores que hay en Visual Code y explicarlos con un comentario

num1=float(input("introduce un número para las operaciones: "))
num2=float(input("introduce otro número para las operaciones: "))

totalSuma=num1+num2
totalResta=num1-num2
totalMultiplicación=num1*num2
totalDivisión=num1/num2

print("El resultado de la suma es: ",totalSuma)
print("El resultado de la resta es: ",totalResta)
print("El resultado de la multiplicación es: ",totalMultiplicación)
print("El resultado de la división es: ",totalDivisión)

totalMódulo=num1%num2
totalPotencia=num1**num2
totalDivisiónEntera=num1//num2

#El módulo nos puede indicar si un número es par o impar
print("El resultado del módulo es: ",totalMódulo)
print("El resultado de la potencia: ",totalPotencia)
print("El resultado de la división entera: ",totalDivisiónEntera)