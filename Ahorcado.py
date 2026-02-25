#ejercicio del ahorcado del Sway.
import random
import time


letrasacento={ "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U" }
#aqui he tenido que convertir la variable en un diccionario de python, un método que he indagado 
#y me ha parecido interesante para usar .get() más adelante
Lista_palabrasecreta=["Guatamalteco", "Alcantarillado", "Imaginación", "Trauma", "Wok", "Silenciador","Centrifugación","Pudrimiento", "Nueve", "Movimiento","Tremebundo","AbsoluteCinema"]
partida="s"
jugadas=0
añadido=""
cantidadLetrasCorrectas=0
print("------------------------------------------------------")
print("                Bienvenido al ahorcado                ")
print("------------------------------------------------------")

while partida=="s":
    modo=3
    tiempoInicial=time.time()
    añadido=input("Quieres añadir una palabra a la lista?: (n/palabra) ").lower() 
    
    if añadido=="n":
        print("Ninguna palabra ha sido añadida")
    elif añadido=="s":
        print(f"Has añadido la palabra {añadido}")
        Lista_palabrasecreta.append(añadido)
    else:
        print("Esa no es una opción válida")
    #así se comprueba si quiere añadir alguna palabra. Me falta por hacer lo de que se borre de Lista_secreta
    Lista_errores=[]
    Lista_aciertos=[]
    palabrasecreta=random.choice(Lista_palabrasecreta)
    print("1. Jugar normal, con palabras y acentos")
    print("2. Jugar sin acentos, ninguna palabra (incluso si normalmente tiene), tendrá acentos")
    while int(modo)>2:
        modo=input("Selecciona uno de los modos: ")
        if modo == "1":
            print("Modo normal seleccionado. Buena suerte")
        elif modo == "2":
            nuevapalabra=""
            for i in range(len(palabrasecreta)):
                a=palabrasecreta[i]
                nuevapalabra+=letrasacento.get(a, a)
                #devuelve la letra sin acento si existe, o la misma letra si no.
            palabrasecreta=nuevapalabra
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

    print(Lista_partida)

    while maxintentos>0:
        jugadas+=1
        letra=input("Intenta adivinar la letra: ")
        if letra.isalpha():
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
            palabraIntento=input("Quieres probar a adivinar la palabra? (n/palabra): ")
            if palabraIntento=="n":
                    print("Vale")
            else:
                palabraIntento=palabraIntento.upper()
                if palabraIntento==palabrasecreta:
                    print(f"¡Has acertado la palabra! Era {palabrasecreta}")
                    maxintentos=0
                    tiempoFinal=time.time()
                    print("")
                    print("Tus resultados de esta partida han sido: ")
                    print("Tus letras acertadas han sido:",Lista_aciertos)
                    print("Tus letras erróneas han sido:",Lista_errores)
                    print(f"Has tardado {round(tiempoFinal-tiempoInicial,2)} segundos")
                    print("Tus intentos se han quedado como...",Lista_partida)
                    print("Y la palabra era",palabrasecreta)
                    print("")
                    partida=input("Quieres jugar otra partida? (s/n) ").lower()
                else:
                    print("Error, la palabra no es la correcta")
            
            if list(palabrasecreta)==Lista_partida:
                print(f"¡Has acertado la palabra! Era {palabrasecreta}")
                maxintentos=0
                tiempoFinal=time.time()
                print("")
                print("Tus resultados de esta partida han sido: ")
                print("Tus letras acertadas han sido:",Lista_aciertos)
                print("Tus letras erróneas han sido:",Lista_errores)
                print(f"Has tardado {round(tiempoFinal-tiempoInicial,2)} segundos")
                print("Tus intentos se han quedado como...",Lista_partida)
                print("Y la palabra era",palabrasecreta)
                print("")
                partida=input("Quieres jugar otra partida? (s/n) ").lower()
            #No sé bien bien qué hacer en los elses, así que pongo un pequeño comentario.
            
            if intentos == 8:
                tiempoFinal=time.time()
                print("Lo siento, te has quedado sin intentos...")
                print("")
                print("Tus resultados de esta partida han sido: ")
                print("Tus letras acertadas han sido:",Lista_aciertos)
                print("Tus letras erróneas han sido:",Lista_errores)
                print(f"Has tardado {tiempoFinal-tiempoInicial} segundos")
                print("Tus intentos se han quedado como...",Lista_partida)
                print("Y la palabra era",palabrasecreta)
                print("")
                partida=input("Quieres jugar otra partida? (s/n) ").lower()
        else:
             print("Por favor, introduce una letra.")
#ThingSpeak - Mathworks: una implantación para hacer estadísticas de victorias, derrotas, etc.