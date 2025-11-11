#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra

palabra=input("Introduce la palabra que quieras recorrer: ")

for i in range (len(palabra)):
    print(f"En la posición {i} está la {palabra[i]}")
