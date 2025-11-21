#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

#He decidido eliminar la variable de control y utilizar otro método para resolver este ejercicio   #varControl=1
#Además de eso, he modificado el programa para hacerlo diferente y mejor
total=0
repeticiones=0

while total <= 50 or total % 2 == 0:
    num1=int(input("Introduce el primer número para sumar: "))
    num2=int(input("Introduce el segundo número para sumar: "))
    print("El resultado de la suma es: ",num1+num2)
    total=total+num1+num2
    repeticiones=repeticiones+1
    if repeticiones==1:
        print(f"El total acumulado es {total} y llevas {repeticiones} operación realizada")
    else:
        print(f"El total acumulado es {total} y llevas {repeticiones} operaciones realizadas")

print("Fin del programa")