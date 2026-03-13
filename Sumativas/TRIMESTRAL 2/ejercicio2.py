palabras=input("Introduce una frase separada por espacios: ")
lista_palabras=palabras.split(" ")

print("Lista de palabras:")
print(lista_palabras)
print("")
#pongo espacios después de cada printeo para que salga más ordenado 

palabra_buscada=input("Qué palabra quieres buscar? ")

veces=lista_palabras.count(palabra_buscada)
if veces==0:
    print(f"La palabra {palabra_buscada} no aparece en la lista")
    print("")
elif veces>1:
    print(f"La palabra {palabra_buscada} aparece {veces} veces")
    print("")
else:
    print(f"La palabra {palabra_buscada} aparece {veces} vez")
    print("")
#A lo mejor esto no era necesario, pero lo he añadido para una mejor funcionalidad del código

frase_nueva=", ".join(lista_palabras)
#esto me confundió bastante al principio (en casa) porque no sabía que habia que poner primero cómo lo quieres separar,
#y después lo que quieres separar
print(frase_nueva)