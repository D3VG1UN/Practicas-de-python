#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.

num=1
mayor=0
menor=0
no99=0

while num!=-99:
    num=int(input("Introduce un número: "))

    if num < menor and not num == -99:
        menor=num
    elif num == -99:
        no99=1

    if num > mayor:
        mayor=num
    

print(f"El mayor es {mayor}")
print(f"el menor es {menor}")
    

    
