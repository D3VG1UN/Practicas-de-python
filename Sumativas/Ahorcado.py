#ejercicio del ahorcado del Sway.
import random
import time


letrasacento={ "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U" }
#aqui he tenido que convertir la variable en un diccionario de python, un método que he indagado 
#y me ha parecido interesante para usar .get() más adelante y así poder programar el modo sin acentos
partidas=0
palabraañadida=""

Lista_palabrasecreta=["Guatamalteco", "Alcantarillado", "Imaginación", "Trauma", "Wok", "Silenciador","Centrifugación","Pudrimiento", "Nueve", "Movimiento","Tremebundo","AbsoluteCinema","Torpedo","Visualización","Mitosis","Ornitorrinco","Yo","Lunes"]
if partidas>0:
    Lista_palabrasecreta.remove(palabraañadida)

jugar="s"
jugadas=0
añadido=""
cantidadLetrasCorrectas=0
print("------------------------------------------------------")
print("                Bienvenido al ahorcado                ")
print("------------------------------------------------------")

while jugar=="s":
    modo=3
    tiempoInicial=time.time()
    
    añadidovalido=0
    while añadidovalido==0:
        añadido=input("Quieres añadir una palabra a la lista?: (n/s) ").lower() 
        if añadido=="n":
            print("Ninguna palabra ha sido añadida")
            print("")
            añadidovalido=1
            partidas+=1
        else:
            if añadido=="s":
                palabraañadida=input("Qué palabra quieres añadir?: ")
                print(f"Has añadido la palabra {palabraañadida}")
                Lista_palabrasecreta.append(palabraañadida)
                añadidovalido=1
                partidas+=1
            else:
                print("Esa no es una respuesta válida. Vuelve a intentarlo.")
                print("")
                añadidovalido=0

    #así se comprueba si quiere añadir alguna palabra, y si no pone ni n ni s, lo vuelve a preguntar
    Lista_errores=[]
    Lista_aciertos=[]
    palabrasecreta=random.choice(Lista_palabrasecreta)
    print("")
    print("Modos de juego: ")
    print("------------------------------------------------------------------------------------")
    print("1. Jugar normal, con palabras y acentos")
    print("2. Jugar sin acentos, ninguna palabra (incluso si normalmente tiene), tendrá acentos")
    print("------------------------------------------------------------------------------------")
    
    while int(modo)>2:
        modo=input("Selecciona uno de los modos: ")
        if modo == "1":
            print("Modo normal seleccionado. Buena suerte")
            print("")
        elif modo == "2":
            nuevapalabra=""
            for i in range(len(palabrasecreta)):
                a=palabrasecreta[i]
                nuevapalabra+=letrasacento.get(a, a)
                #devuelve la letra sin acento si existe, o la misma letra si no.
            palabrasecreta=nuevapalabra
            print("Modo sin acentos seleccionado. Buena suerte.")
            print("")
        elif modo == "":
            print("Por intentar introducir un espacio, jugarás con acentos")
            print("")
            modo=1
        else:
            print("Ese modo de juego no existe")
            modo=input("Selecciona uno de los modos: ")
            

    palabrasecreta=palabrasecreta.upper()
    #print(palabrasecreta)
    Lista_partida=[]
    Lista_ahorcado=[]
    Lista_ahorcado_letras=["A","H","O","R","C","A","D","O"]
    Palabrasecreta_lista=[]
    intentos=0
    maxintentos=8
    palabraIntento=""
    menu=""
    cantidadLetrasTotales=len(palabrasecreta)
    #me gusta trabajar inicializando todas las variables al principio

    for i in palabrasecreta:
        Lista_partida.append("_")
        Palabrasecreta_lista.append(i)

    while maxintentos>0:
        jugadas+=1
        print("")
        print(Lista_partida)
        letra=input("Intenta adivinar la letra: ")
        print("")
        if letra.isalpha() and len(letra)==1:
            #como he mencionado en el word, compruebo si está en el ALFAbeto. *guiño guiño*
            letra=letra.upper()

            if letra in Lista_aciertos:
                print("Ya has introducido esa letra. ")
                Lista_ahorcado.append(Lista_ahorcado_letras[intentos])
                intentos+=1
                maxintentos-=1
                Lista_errores.append(letra)
                print(f"Te quedan {8-intentos} intentos")
                print(Lista_ahorcado)
                print("Letras incorrectas o repetidas:",Lista_errores)
                print("Letras correctas:",Lista_aciertos)
                print("")
            elif letra in Lista_errores:
                if letra in palabrasecreta:
                    print("Ya has introducido esa letra. ")
                    Lista_ahorcado.append(Lista_ahorcado_letras[intentos])
                    intentos+=1
                    maxintentos-=1
                    print(f"Te quedan {8-intentos} intentos")
                    print(Lista_ahorcado)
                    print(Lista_partida)
                    Lista_errores.append(letra)
                    print("")
            #para esto, he copiado el código de cuando fallas.
            else:
                if letra in palabrasecreta:
                    for n in range(len(palabrasecreta)):
                        if palabrasecreta[n]==letra:
                            Lista_partida[n]=letra      
                            #aquí compruebo si la letra en esa posición es la misma que la que ha introducido
                    print("¡Has encontrado una letra!")
                    print(Lista_partida)
                    Lista_aciertos.append(letra)
                    print("Letras incorrectas o repetidas:",Lista_errores)
                    print("Letras correctas:",Lista_aciertos)
                else:
                    Lista_ahorcado.append(Lista_ahorcado_letras[intentos])
                    intentos+=1
                    maxintentos-=1
                    print("No está en la palabra...")
                    Lista_errores.append(letra)
                    print(f"Te quedan {8-intentos} intentos")
                    print(Lista_ahorcado)
                    print("Letras incorrectas o repetidas:",Lista_errores)
                    print("Letras correctas:",Lista_aciertos)
                    print("")
            palabraIntento=input("Quieres probar a adivinar la palabra? (n/palabra): ")
            if palabraIntento=="n":
                    print("Vale")
            else:
                palabraIntento=palabraIntento.upper()
                if palabraIntento==palabrasecreta:
                    print(f"¡Has acertado la palabra! Era {palabrasecreta}")
                    maxintentos=0
                    tiempoFinal=time.time()
                    tiempoTotal=tiempoFinal-tiempoInicial
                    tiempoMinutos=tiempoTotal//60
                    tiempoSegundos=round(tiempoTotal%60, 2)
                    print("")
                    print("Tus resultados de esta partida han sido: ")
                    print("Tus letras acertadas han sido:",Lista_aciertos)
                    print("Tus letras erróneas han sido:",Lista_errores)
                    print(f"Has tardado {tiempoMinutos} minutos y {tiempoSegundos} segundos")
                    print("Tus intentos se han quedado como...",Lista_partida)
                    print("Y la palabra era",palabrasecreta)
                    print("")
                    jugar=input("Quieres jugar otra partida? (s/n) ").lower()
                else:
                    print("Error, la palabra no es la correcta")
            
            if list(palabrasecreta)==Lista_partida:
                print(f"¡Has acertado la palabra! Era {palabrasecreta}")
                maxintentos=0
                tiempoFinal=time.time()
                tiempoTotal=tiempoFinal-tiempoInicial
                tiempoMinutos=tiempoTotal//60
                tiempoSegundos=round(tiempoTotal%60,2)
                print("")
                print("Tus resultados de esta partida han sido: ")
                print("Tus letras acertadas han sido:",Lista_aciertos)
                print("Tus letras erróneas han sido:",Lista_errores)
                print(f"Has tardado {tiempoMinutos} minutos y {tiempoSegundos} segundos")
                print("Tus intentos se han quedado como...",Lista_partida)
                print("Y la palabra era",palabrasecreta)
                print("")
                jugar=input("Quieres jugar otra partida? (s/n) ").lower()
            
            if intentos == 8:
                tiempoFinal=time.time()
                tiempoTotal=tiempoFinal-tiempoInicial
                tiempoMinutos=tiempoTotal//60
                tiempoSegundos=round(tiempoTotal%60,2)
                #el código es el mismo - división entera para los minutos, y lo que sobra son los segundos
                print("Lo siento, te has quedado sin intentos...")
                print("")
                print("Tus resultados de esta partida han sido: ")
                print("Tus letras acertadas han sido:",Lista_aciertos)
                print("Tus letras erróneas han sido:",Lista_errores)
                print(f"Has tardado {tiempoMinutos} minutos y {tiempoSegundos} segundos")
                print("Tus intentos se han quedado como...",Lista_partida)
                print("Y la palabra era",palabrasecreta)
                print("")
                jugar=input("Quieres jugar otra partida? (s/n) ").lower()
        else:
             print("Por favor, introduce una letra.")

print("Partidas finalizadas")