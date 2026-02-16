#ejercicio 21. intervalos II
#a1≤b1 and a2≤b2


intervalos=input()
listaintervalos=intervalos.split()

num1=int(listaintervalos[0])
num2=int(listaintervalos[1])
num3=int(listaintervalos[2])
num4=int(listaintervalos[3])

salida=[]

if num1==num3 and num2==num4:
    print("=")
else:
    if num2<=num4 and num1>=num3:
        print(1)
    elif num2>=num4 and num1<=num3:
        print(2)
    else:
        print("?")

