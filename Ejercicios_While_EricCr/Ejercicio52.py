#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While

num1=float(input("Introduce el primer número para sumar: "))
num2=float(input("Introduce el segundo número para sumar: "))
varControl=1
decision=""

while varControl==1:
    print("El resultado de la suma es: ",num1+num2)
    decision=input("¿Deseas repetir la operación? (s/n) ")
    if decision=="s":
        num1=float(input("Introduce el primer número para sumar: "))
        num2=float(input("Introduce el segundo número para sumar: "))
    elif decision=="n":
        varControl=2
    else: 
        print("Haber introducido una opción correcta.")
        varControl=3
print("Programa finalizado")

