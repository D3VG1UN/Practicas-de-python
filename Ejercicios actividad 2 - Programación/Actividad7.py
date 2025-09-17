#programa que calcule dos operandos con los 7 operadores vistos en clase. 
#¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

operador1=float(input("Introduce un número para las operaciones: "))
operador2=float(input("Introduce el segundo valor: "))

totalSuma=operador1+operador2
totalResta=operador1-operador2
totalMultiplicación=operador1*operador2
totalDivisión=round(operador1/operador2, 2)
totalMódulo=operador1%operador2
totalPotencia=operador1**operador2
totalDivisiónEntera=operador1//operador2

print(f"El resultado de la división es de {totalDivisión}")