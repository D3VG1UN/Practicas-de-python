#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista

repetir="s"
letra=""
milista=[]

while repetir == "s":
    letra=input("Introduce una letra: ")
    
    if letra.isalpha():
            if letra in "àáä":
                letra="a"
            elif letra in "éèë":
                letra="e"
            elif letra in "íìï":
                letra="i"
            elif letra in "óòö":
                letra="o"
            elif letra in "úùü":
                letra="u"
            else:
                letra=letra
            
            if letra not in milista:
                milista.append(letra)
                repetir=input("Quieres introducir otra letra? (s/n): ")
            else:
                print("Letra repetida")
    else:
        repetir="s"

print(milista)