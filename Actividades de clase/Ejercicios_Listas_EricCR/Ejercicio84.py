#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.
import random

lista1=["casa","barco","gato","perro","madera","agua","puente","pantalón"]

randomnum=random.randint(0,7)
palabra=lista1[randomnum]
desordenada=list(palabra)
random.shuffle(desordenada)
#he buscado un método para barajar las letras correctamente

intento=""
intentos=3

while intentos>0:
    print(desordenada)
    intento=input("Cual es la palabra? ")
    if intento == palabra:
        print("ACERTASTE")
        intentos=0
    else:
        print("Fallaste")
        intentos-=1
print("Te quedaste sin intentos. La palabra era", palabra)