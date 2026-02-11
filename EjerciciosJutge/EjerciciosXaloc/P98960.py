#ejercicio 11. mayusculas y minusculas
import string

letra=input()
minusculas="qwertyuiopasdfghjklñçzxcvbnm"
mayusculas=minusculas.upper()

if letra in minusculas:
    letra=letra.upper()
    print(letra)
elif letra in mayusculas:
    letra=letra.lower()
    print(letra)
else:
    print("Enter a letter")