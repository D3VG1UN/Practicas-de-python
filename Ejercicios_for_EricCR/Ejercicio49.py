# A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

palabra=input("Introduce la palabra 'secreta': ")
letra=input("Introduce la letra: ")
posiciones=[]
posicionestotales=palabra.count(letra)

for i in range(len(palabra)):
    if palabra[i].lower==letra.lower:
        posiciones.append(i+1)
    print("La letra existe")
    print(f"La letra se encuentra en la/s posicion/es {posiciones}")
