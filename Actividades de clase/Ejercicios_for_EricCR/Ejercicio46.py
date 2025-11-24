#A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.

palabra=input("Introduce una palabra: ")
#palabra=palabra.lower()
vocales="aeiouAEIOUáéíóúÁÉÍÓÚ"
#vocales="aeiouáéíóú"
varVocales=""
varConsonantes=""

for i in range (len(palabra)):
    if palabra[i] in vocales:
        varVocales=varVocales+palabra[i]
    else:
        varConsonantes=varConsonantes+palabra[i]

print(f"Las vocales de la palabra {palabra} son: {varVocales}")
print(f"Las consonantes de la palabra {palabra} son: {varConsonantes}")
#Es el mismo código que el anterior, pero en el caso de que me saliera el error, lo que haría sería establecer la palabra como
#palabra.lower() para que las letras se hicieran minúsculas. Pongo con comentarios lo que habría hecho.