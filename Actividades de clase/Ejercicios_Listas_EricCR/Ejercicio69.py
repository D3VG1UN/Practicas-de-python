#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor

respuesta="s"
mi_lista=[]
num=0

while respuesta == "s":
    num=int(input("Introduce un valor para añadir a la lista: "))
    mi_lista.append(num)
    respuesta=input("Quieres introducir otro número? (s/n): ")

mi_lista.sort()
#.sort() ordena los números, de menor a mayor
print(mi_lista)