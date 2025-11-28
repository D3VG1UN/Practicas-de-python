#actividad 4. var_total = 50. Si el número introducido es par, se sumará, si es impar, se restará. El programa se finalizará cuando
#el número introducido sea 0 o var_total sea mayor que 60. 

var_total=50
repetir=1

#voy a usar bucle while para que, cuando una de las condiciones de fin se cumpla, cambie el valor de la variable y se acabe.
while repetir == 1:
    num=int(input("Introduce el número: "))

    if num == 0:
        print("Fin del programa. El valor introducido es 0.")
        repetir=0
        #me gustaría añadir un comentario extra para saber el motivo por el que finaliza el programa
    else:
            if num%2==0:
                var_total+=num
                print(var_total)
            elif num%2!=0:
                var_total-=num
                print(var_total)
            
            if var_total>60:
                print("Fin del programa. El valor total es mayor que 60.")
                repetir=0