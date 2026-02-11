#ejercicio 12. clasificación
import string

vocales="aeiouAEIOUáéíóúÁÉÍÚÓ"
letra=input()

if letra.isupper():
    print("uppercase")
else:
    print("lowercase")

if letra in vocales:
    print("vowel")
else:
    print("consonant")