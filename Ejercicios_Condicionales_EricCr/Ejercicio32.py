#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas.

#primero, pasaré toda la frase a minúsculas, y después haré lo mismo con laas palabras, para que no haya
#diferencia en la palabra que se introduzca
frase=str("A quién madruga Dios ayuda")
fraseminuscula=frase.lower()

palabra=str(input("Introduce la palabra que quieres encontrar en la frase: "))
palabraminuscula=palabra.lower()

posicion=fraseminuscula.rfind(palabraminuscula)

if posicion >=0:
    print(f"La palabra está en la frase y está en el índice {posicion}")
else:
    print("La palabra no está en la frase.")

#prueba:
#print(fraseminuscula)
#print(palabraminuscula)