#Busca Internet qué función permite obtener la longitud de un String, realiza un programa 
#que al introducir una frase devuelva la longitud

frase=input("Introduce una frase:")

#La longitud de una frase, es decir, "Length" en inglés se utiliza con el método "len", que sirve para contar automáticamente
#todos los caracteres en una frase
LongitudFrase=len(frase)

print(f"La longitud de la frase es {LongitudFrase}")