#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
num1=float(input("Introduce el primer número para sumar: "))
num2=float(input("Introduce el segundo número para sumar: "))
varControl=1
decision=""
total=0
repeticiones=0

while varControl==1:
    print("El resultado de la suma es: ",num1+num2)
    total=total+num1+num2
    repeticiones=repeticiones+1
    decision=input("¿Deseas repetir la operación? (s/n) ")
    if decision=="s":
        num1=float(input("Introduce el primer número para sumar: "))
        num2=float(input("Introduce el segundo número para sumar: "))
    elif decision=="n":
        varControl=2
    else: 
        print("Haber introducido una opción correcta.")
        varControl=3
print("Resumen:")
print(f"La suma total es {total} y el número de repeticiones es: {repeticiones}")