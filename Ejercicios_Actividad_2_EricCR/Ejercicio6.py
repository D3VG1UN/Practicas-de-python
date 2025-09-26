# A partir del programa 5. Haz que se muestre por pantalla también 
#la frase en el orden inverso en que se han introducido las palabras.

palabra1=input("Introduce una palabra para formar una frase: ")
palabra2=input("Introduce otra palabra: ")
palabra3=input("Introduce otra palabra más: ")
palabra4=input("Introduce otra palabra: ")
palabra5=input("Introduce la última palabra: ")

print(f"{palabra1}{palabra2}{palabra3}{palabra4}{palabra5}")
print(f"{palabra5}{palabra4}{palabra3}{palabra2}{palabra1}")