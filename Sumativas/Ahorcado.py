#ejercicio del ahorcado del Sway.
import random
import time


letrasacento={ "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U" }
#aqui he tenido que convertir la variable en un diccionario de python, un método que he indagado 
#y me ha parecido interesante para usar .get() más adelante y así poder programar el modo sin acentos
partidas=0
palabraañadida=""
tauntTotal=0

Lista_palabrasecreta=["Guatamalteco", "Alcantarillado", "Imaginación", "Trauma", "Wok", "Silenciador","Centrifugación","Pudrimiento", "Nueve", "Movimiento","Tremebundo","AbsoluteCinema","Torpedo","Visualización","Mitosis","Ornitorrinco","Yo","Lunes","Cerebelo","Asteriscos","Carlos","Minvar"]


jugar="s"
jugadas=0
añadido=""
cantidadLetrasCorrectas=0
print("------------------------------------------------------")
print("                Bienvenido al ahorcado                ")
print("------------------------------------------------------")
victorias=0
derrotas=0

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
    if palabrasecreta==palabraañadida:
        Lista_palabrasecreta.remove(palabraañadida)
    print("")
    print("Modos de juego: ")
    print("------------------------------------------------------------------------------------")
    print("1. Jugar normal, con palabras y acentos")
    print("2. Jugar sin acentos, ninguna palabra (incluso si normalmente tiene), tendrá acentos")
    print("------------------------------------------------------------------------------------")
    taunt=0

    while modo!="seguir":
        modo=input("Selecciona uno de los modos: ")
        if len(modo)==1:
            if modo == "1":
                print("Modo normal seleccionado. Buena suerte")
                print("")
                modo="seguir"
            elif modo == "2":
                nuevapalabra=""
                for i in range(len(palabrasecreta)):
                    a=palabrasecreta[i]
                    nuevapalabra+=letrasacento.get(a, a)
                    #devuelve la letra sin acento si existe, o la misma letra si no.
                palabrasecreta=nuevapalabra
                print("Modo sin acentos seleccionado. Buena suerte.")
                print("")
                modo="seguir"
            elif modo == "":
                print("Por intentar introducir un espacio, jugarás con acentos")
                print("")
                modo="seguir"
            else:
                print("Ese modo de juego no existe")
                modo=input("Selecciona uno de los modos: ")
        else:
            
            if tauntTotal==0:    
                print("Longitud incorrecta. Si vuelves a intentar introducir más de un número, te pondré la palabra más larga que conozca.")
                taunt+=1
                if taunt==2:
                    print("Y mira que te lo advertí")
                    tauntTotal+=1
                    palabrasecreta="Electroencefalografista"
                    modo="seguir"
            elif tauntTotal==1:
                print("Tío...")
                palabrasecreta="Ácidodesoxiribonucleico"
                modo="seguir"
                dos="si"
                tauntTotal+=1
            else:
                tauntTotal=3

    if tauntTotal>2:
        break
    palabrasecreta=palabrasecreta.upper()
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
            #compruebo si está en el ALFAbeto. *guiño guiño*
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
                    print("¡Has acertado la palabra!")
                    victorias+=1
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
                    print("Victorias:",victorias)
                    print("Derrotas:",derrotas)
                    print("")
                    fecha=time.ctime()
                    #con "a" se crea un nuevo fichero, donde se almacenarán los datos
                    #además, se posiciona al final, por lo que cada partida se guardará
                    archivo_texto=open("DatosPartida.txt", "a")
                    #usaré \n para hacer un salto de línea y que no se ponga todo en la misma
                    #la función .write() hace... pues eso, escribir
                    archivo_texto.write("Palabra secreta: " + palabrasecreta + ", ")
                    archivo_texto.write("Letras acertadas: " + str(Lista_aciertos) + ", ")
                    archivo_texto.write("Letras incorrectas: " + str(Lista_errores) + ", ")
                    archivo_texto.write("Intentos realizados: " + str(jugadas) + ", ")
                    archivo_texto.write("Fecha de la partida: " + str(fecha))
                    archivo_texto.write("\n")
                    print("")
                    #y close() cierra y guarda el archivo 
                    archivo_texto.close()
                    print("La información ha sido guardada en un archivo txt")
                    print("")
                    jugar=input("Quieres jugar otra partida? (s/n) ").lower()
                else:
                    print("Error, la palabra no es la correcta")
            
            if list(palabrasecreta)==Lista_partida:
                print(f"¡Has acertado la palabra! Era {palabrasecreta}")
                victorias+=1
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
                print("")
                print("Victorias:",victorias)
                print("Derrotas:",derrotas)
                print("")
                fecha=time.ctime()
                #con "a" se crea un nuevo fichero, donde se almacenarán los datos
                #además, se posiciona al final, por lo que cada partida se guardará
                archivo_texto=open("DatosPartida.txt", "a")
                #usaré \n para hacer un salto de línea y que no se ponga todo en la misma
                #la función .write() hace... pues eso, escribir
                archivo_texto.write("Palabra secreta: " + palabrasecreta + ", ")
                archivo_texto.write("Letras acertadas: " + str(Lista_aciertos) + ", ")
                archivo_texto.write("Letras incorrectas: " + str(Lista_errores) + ", ")
                archivo_texto.write("Intentos realizados: " + str(jugadas) + ", ")
                archivo_texto.write("Fecha de la partida: " + str(fecha))
                archivo_texto.write("\n")
                #y close() cierra y guarda el archivo 
                archivo_texto.close()
                print("La información ha sido guardada en un archivo txt")
                print("")
                jugar=input("Quieres jugar otra partida? (s/n) ").lower()
            
            if intentos == 8:
                derrotas+=1
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
                print("Victorias:",victorias)
                print("Derrotas:",derrotas)
                print("")
                fecha=time.ctime()
                #con "a" se crea un nuevo fichero, donde se almacenarán los datos
                #además, se posiciona al final, por lo que cada partida se guardará
                archivo_texto=open("DatosPartida.txt", "a")
                #usaré \n para hacer un salto de línea y que no se ponga todo en la misma
                #la función .write() hace... pues eso, escribir
                archivo_texto.write("Palabra secreta: " + palabrasecreta + ", ")
                archivo_texto.write("Letras acertadas: " + str(Lista_aciertos) + ", ")
                archivo_texto.write("Letras incorrectas: " + str(Lista_errores) + ", ")
                archivo_texto.write("Intentos realizados: " + str(jugadas) + ", ")
                archivo_texto.write("Fecha de la partida: " + str(fecha))
                archivo_texto.write("\n")
                #y close() cierra y guarda el archivo 
                archivo_texto.close()
                print("")
                print("La información ha sido guardada en un archivo txt")
                print("")
                jugar=input("Quieres jugar otra partida? (s/n) ").lower()
        else:
             print("Por favor, introduce una letra.")

print("Partidas finalizadas")