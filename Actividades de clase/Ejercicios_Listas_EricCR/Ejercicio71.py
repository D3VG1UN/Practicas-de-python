#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.

repetir="s"
letra=""
milista=[]

while repetir == "s":
    letra=input("Introduce una letra ")
    if not letra.isnumeric():
        milista.append(letra)
    else:
        repetir=="s"