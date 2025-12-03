#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
num=0
impares=0
pares=0
positivos=0
negativos=0
total=0

while num!=-99:
    num=int(input("Introduce un número: "))
    total+=num
    if num % 2 == 0:
        pares+=1
    elif num % 2 != 0:
        impares+=1
    
    if num<0:
        negativos+=1
    elif num>=0:
        positivos+=1
    
print(f"La cantidad de positivos es {positivos}")
print(f"La cantidad de negativos es {negativos-1}")
print(f"La cantidad de pares es {pares}")
print(f"La cantidad de impares es {impares-1}")
print(f"El total es: {total+99}")