#actividad DNI sumativa
import string

dni=""
letrasdni=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
letralista=""
pregunta="s"
lista_intentos=[]
lista_correctos=[]
lista_incorrectos=[]
dnicorrecto=""
dniincorrecto=""
totalerrores=0
totalaciertos=0
menu=""

while pregunta=="s":
    dni=input("Introduce tu DNI: ")
    if len(dni)==8:
        if dni.isnumeric():
            letra=int(dni)%23
            if letrasdni[letra] in letrasdni:
                letralista=letrasdni[letra]
                print(dni,"-",letralista)
                #imprime el número, un espacio y las letras.
                dnicorrecto=dni + "-" + letralista
                lista_intentos.append(3)
                lista_correctos.append(dnicorrecto)
            else:
                print("No se puede introducir ese DNI")
                dniincorrecto=dni
                lista_incorrectos.append(dniincorrecto)
                lista_intentos.append(2)
        else:
            print("Introduzca números, por favor")
            dniincorrecto=dni
            lista_incorrectos.append(dniincorrecto)
            lista_intentos.append(1)
    else:
        print("Los números no cumplen con la longitud requerida")
        dniincorrecto=dni
        lista_incorrectos.append(dniincorrecto)
        lista_intentos.append(0)
    #estos números me sirven para saber la cantidad de errores y sus tipos
    pregunta=input("Desea continuar introduciendo DNIs? (s/n): ")



lista_correctos.sort()
lista_incorrectos.sort()
totalerrores=len(lista_incorrectos)
totalaciertos=len(lista_correctos)
totaltotal=totalaciertos+totalerrores
porcentajecorrectos=round((totalaciertos/totaltotal)*100,1)
porcentajeincorrectos=100-porcentajecorrectos
#todos los errores de longitud están recogidos en la lista intentos, con 0, así que con el método .count() puedo ver cuántas veces
#aparece este error y dividirlo entre la cantidad total de errores
porcentajeerroreslen=round((lista_intentos.count(0)/len(lista_intentos))*100, 1)
porcentajeerroresnum=round((lista_intentos.count(1)/len(lista_intentos))*100, 1)
porcentajeerroresex=round((lista_intentos.count(2)/len(lista_intentos))*100, 1)
#tuve un problema, y es que me olvidé de multiplicar por cien, pro lo que me salían demasiado pequeños

print("")
print("OPCIONES")
print("1. Listar NIF correcto ordenado de menor a mayor")
print("2. Listar DNI incorrecto ordenado de menor a mayor")
print("3. Número total de errores producidos")
print("4. Número total de DNI correctos")
print("5. Porcentaje intentos con errores o sin")
print("6. Salir (s/n)")

while pregunta=="n":
    print("")
    menu=int(input("Introduce una de las opciones proporcionadas: "))
    print("")
    if menu == 1:
        print(lista_correctos)
    elif menu == 2:
        print(lista_incorrectos)
    elif menu == 3:
        print(totalerrores)
    elif menu == 4:
        print(totalaciertos)
    elif menu == 5:
        print(f"El número de intentos es: {len(lista_intentos)}")
        print(f"El porcentaje de dnis correctos es: {porcentajecorrectos}%")
        print(f"El porcentaje de dnis incorrectos es: {porcentajeincorrectos}%")
        print(f"El porcentaje de errores de longitud es: {porcentajeerroreslen}%")
        print(f"El porcentaje de errores de números es: {porcentajeerroresnum}%")
        print(f"El porcentaje de errores de existencia es: {porcentajeerroresex}%")
    elif menu == 6:
        print("Programa finalizado")
        pregunta="fin"
    