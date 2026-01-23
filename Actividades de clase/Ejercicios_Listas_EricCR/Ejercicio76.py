#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo
import string

lista1=["a","b","D","x","r","X",3,"h","w",2,"i"]
listanums=[]
listaletras=[]
mayus="QWERTYUIOPASDFGHJKLÑÇZCVBNMÉÚÍÓÁÈÙÌÒÀËÜÏÖÄ"


for i in lista1:
    if str(i).isnumeric():
        listanums.append(i)
    
    if str(i).isalpha():
        listaletras.append(i)
    
    if str(i) in mayus:
        str(i).lower()
        listaletras.append(i)

orden=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
if orden == 1:
    listanums.sort()
    listaletras.sort()
    print(listanums)
    print(listaletras)
elif orden == 2:
    listaletras.sort(reverse=True)
    listanums.sort(reverse=True)
    print(listaletras)
    print(listanums)
    #he buscado en internet una manera de invertirlo, y sólo he encontrado este
    #también he visto el método "reverse", pero ese sólo no lo ordene