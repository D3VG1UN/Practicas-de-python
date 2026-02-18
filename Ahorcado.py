#ejercicio del ahorcado del Sway
import random

Lista_palabrasecreta=["Guatamalteco", "Alcantarillado", "Imaginación", "Trauma", "Wok", "Silenciador","Centrifugación","Pudrimiento", "Nueve", "Movimiento","Tremebundo","AbsoluteCinema"]
partida="s"
jugadas=0
añadido=""
print("------------------------------------------------------")
print("                Bienvenido al ahorcado                ")
print("------------------------------------------------------")

while partida=="s":
    print("Introduce la letra 'l' cuando te den la opción para visualizar las letras falladas")
    if jugadas>0:
        añadido=input("Quieres añadir una palabra a la lista?: (n/palabra) ").lower()
    else:
        print("Pásatelo bien")
    
    if añadido=="n":
        print("Ninguna palabra ha sido añadida")
    else:
        if añadido=="":
            print("Primera partida, eh?")
        else:
            print(f"Has añadido la palabra {añadido}")
            Lista_palabrasecreta.append(añadido)
    Lista_letrasmal=[]
    palabrasecreta=random.choice(Lista_palabrasecreta)
    palabrasecreta=palabrasecreta.upper()
    #print(palabrasecreta)
    Lista_partida=[]
    Lista_ahorcado=[]
    Palabrasecreta_lista=[]
    intentos=0
    maxintentos=8
    palabraIntento=""
    menu=""
    
    for i in palabrasecreta:
        Lista_partida.append("_")
        Palabrasecreta_lista.append(i)

    print(Lista_partida)

    while maxintentos>0:
        jugadas+=1
        letra=input("Intenta adivinar la letra: ")
        letra=letra.upper()
        if letra in palabrasecreta:
            for n in range(len(palabrasecreta)):
                if palabrasecreta[n]==letra:
                    Lista_partida[n]=letra      
            print("¡Has encontrado una letra!")
            print(Lista_partida)
        else:
            intentos+=1
            maxintentos-=1
            print("No está en la palabra...")
            Lista_letrasmal.append(letra)
            print(f"Te quedan {8-intentos} intentos")
        menu=input("Quieres ver la lista de letras incorrectas? (l/n)")
            #por acabar de añadir lo del menú
        palabraIntento=input("Quieres probar a adivinar la palabra? (n/palabra): ")
        if palabraIntento=="n":
                print("Vale")
        else:
            palabraIntento=palabraIntento.upper()
            if palabraIntento==palabrasecreta:
                print(f"¡Has acertado la palabra! Era ")
                maxintentos=0
                partida=input("Quieres jugar otra partida? (s/n)").lower()
            else:
                print("Error, la palabra no es la correcta")
        
        if intentos == 8:
            print("Lo siento, te has quedado sin intentos...")
            partida=input("Quieres jugar otra partida? (s/n)").lower()
