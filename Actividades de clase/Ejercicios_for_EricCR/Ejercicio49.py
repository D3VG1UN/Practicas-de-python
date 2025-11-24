# A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

palabra=input("Introduce la palabra 'secreta': ")

for i in range(len(palabra)):
    letra=input("Introduce una letra: ")
    contador=0
    #Utilizamos el contador para ver cuántas veces aparece la letra en la palabra.  
    for j in range(len(palabra)):
        if palabra[j] == letra:
            print(f"La letra se encuentra en la posición {j + 1}")
            contador=contador + 1

    if contador == 0:
        print("La letra no aparece en la palabra")
