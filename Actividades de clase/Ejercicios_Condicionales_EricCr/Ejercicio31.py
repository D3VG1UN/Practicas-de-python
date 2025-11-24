#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.

frase=str("A quién madruga Dios ayuda")

palabra=str(input("Introduce la palabra que quieres encontrar en la frase: "))
posicion=frase.rfind(palabra)

if posicion >=0:
    print(f"La palabra está en la frase y está en el índice {posicion}")
else:
    print("La palabra no está en la frase.")
