import string

palabra=input("Introduce la palabra 'secreta': ")
palabra=palabra.lower()
letra=""                                      #input("Introduce la letra: ")
letra=letra.lower()
#posicion=palabra.find(letra)
#posicion2=palabra.count(letra)

for i in range (len(palabra)):
    letra=input("Introduce una letra: ")
    posicion=palabra.find(letra)
    posicion2=palabra.count(letra)
    if letra in palabra:
        print("La letra existe")
        if posicion2==1:
            posicion=posicion+1
            print(f"La letra {letra} se encuentra en la posición {posicion}")
    else:
        print("La letra no existe")



print(posicion, posicion2)