#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:

palabra=input("Introduce una palabra: ")
vocales="aeiouAEIOUáéíóúÁÉÍÓÚ"
varVocales=""
varConsonantes=""

for i in range (len(palabra)):
    if palabra[i] in vocales:
        varVocales=varVocales+palabra[i]
    else:
        varConsonantes=varConsonantes+palabra[i]

print(f"Las vocales de la palabra {palabra} son: {varVocales}")
print(f"Las consonantes de la palabra {palabra} son: {varConsonantes}")