#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While

num1=int(input("Introduce el primer número para sumar: "))
num2=int(input("Introduce el segundo número para sumar: "))
varControl=1
decision=""
total=0
repeticiones=0

while varControl==1:
    print("El resultado de la suma es: ",num1+num2)
    total=total+num1+num2
    repeticiones=repeticiones+1
    if repeticiones==1:
        print(f"El total acumulado es {total} y llevas {repeticiones} operación realizada")
    else:
        print(f"El total acumulado es {total} y llevas {repeticiones} operaciones realizadas")
    
    if total < 50:
        num1=int(input("Introduce el primer número para sumar: "))
        num2=int(input("Introduce el segundo número para sumar: "))
    else: 
        varControl=2
print("Fin del programa")