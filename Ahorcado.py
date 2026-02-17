#ejercicio del ahorcado del Sway
import random

Lista_palabrasecreta=["Guatamalteco", "Alcantarillado", "Imaginación", "Trauma", "Wok", "Silenciador","Centrifugación","Pudrimiento", "Nueve", "Movimiento"]
palabrasecreta=Lista_palabrasecreta[random.randint(0, 9)]
print(palabrasecreta)
Lista_partida=[]
Lista_ahorcado=[]
Palabrasecreta_lista=[]

for i in palabrasecreta:
    Lista_partida.append("_")
    Palabrasecreta_lista.append(i)

print(Lista_partida)

for x in range (8):
    letra=input("Intenta adivinar la letra: ")
    if letra in palabrasecreta:
        for n in range(len(palabrasecreta)):
            if palabrasecreta[n]==letra:
                Lista_partida[n]=letra
                print("Una letra acertada")
                print(Lista_partida)
        