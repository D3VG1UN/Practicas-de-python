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
                #este proceso es optimizable, haciendo la variable antes, pero me gusta dejarlo así
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

    pregunta=input("Desea continuar introduciendo DNIs? (s/n): ")

while pregunta=="n"
print("")
print("OPCIONES")
print("1. Listar NIF correcto ordenado de menor a mayor")
print("2. Listar DNI incorrecto ordenado de menor a mayor")
print("3. Número total de errores producidos")
print("4. Número total de DNI correctos")
print("5. Porcentaje intentos con errores o sin")
print("6. Salir (s/n)")
menu=int(input("Introduce una de las opciones proporcionadas: "))

print("")

lista_correctos.sort()
lista_incorrectos.sort()
totalerrores=len(lista_incorrectos)
totalaciertos=len(lista_correctos)
totaltotal=totalaciertos+totalerrores
porcentajecorrectos=round((totalaciertos/totaltotal),2)
porcentajeincorrectos=100-porcentajecorrectos
#todos los errores de longitud están recogidos en la lista intentos, con 0, así que con el método .count() puedo ver cuántas veces
#aparece este error y dividirlo entre la cantidad total de errores
porcentajeerroreslen=round((lista_intentos.count(0)/len(lista_intentos)), 2)
porcentajeerroresnum=round((lista_intentos.count(1)/len(lista_intentos)), 2)
porcentajeerroresex=round((lista_intentos.count(2)/len(lista_intentos)), 2)



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
    print(f"El porcentaje de dnis correctos son: {porcentajecorrectos}%")
    #por hacer: acabar lo del DNI y añadir el bucle while