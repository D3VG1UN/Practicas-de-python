#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.

repetir="s"
letra=""
milista=[]

while repetir == "s":
    letra=input("Introduce una letra: ")
    if letra.isalpha():
        if letra not in milista:
            milista.append(letra)
            repetir=input("Quieres introducir otra letra? (s/n): ")
    else:
        repetir="s"

print(milista)