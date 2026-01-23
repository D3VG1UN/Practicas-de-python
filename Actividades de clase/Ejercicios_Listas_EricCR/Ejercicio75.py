#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#           a. Cantidad total de valores
#           b. Cantidad de números
#           c. Cantidad de letras
#           d. Cantidad de mayúsculas
#           e. Suma de los valores numéricos
import string

lista1=["a","b","D","x","r","X",3,"h","w",2,"i"]
totalvalores=0
nums=0
letras=0
mayus="QWERTYUIOPASDFGHJKLÑÇZXCVBNM"
nummayus=0
sumanums=0

for i in lista1:
    totalvalores+=1
    
    if str(i).isnumeric():
        nums+=1
        sumanums+=i
    
    if str(i).isalpha():
        letras+=1
    
    if str(i) in mayus:
        nummayus+=1

print(f"Número de valores: {totalvalores}")
print(f"Cantidad de números: {nums}")
print(f"Cantidad de letras: {letras}")
print(f"Cantidad de mayúsculas: {nummayus}")
print(f"Suma total de numeros: {sumanums}")

    