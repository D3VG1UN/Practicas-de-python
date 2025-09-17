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

print(f"El resultado de la suma es de {totalSuma}")
print(f"El resultado de la resta es de {totalResta}")
print(f"El resultado de la multiplicación es de {totalMultiplicación}")
print(f"El resultado de la división es de {totalDivisión}")
print(f"El resultado del módulo es de {totalMódulo}")
print(f"El resultado de la potencia es de {totalPotencia}")
print(f"El resultado de la división entera es de {totalDivisiónEntera}")
