# ejercicio 19. intervalos I

intervalos=input()
listaintervalos=intervalos.split()

num1=int(listaintervalos[0])
num2=int(listaintervalos[1])
num3=int(listaintervalos[2])
num4=int(listaintervalos[3])

salida=[]

if num2<num3:
    salida=[]
elif num4<num1:
    salida=[]

else:
    if num1>num3:
        if num4>num2:
            salida.append(num1)
            salida.append(num2)

        if num4<num2:
            salida.append(num1)
            salida.append(num4)

        if num4==num2:
            salida.append(num1)
            salida.append(num2)

    elif num1<num3:
        if num4>num2:
            salida.append(num3)
            salida.append(num2)

        if num2>num4:
            salida.append(num3)
            salida.append(num4)

        if num2==num4:
            salida.append(num3)
            salida.append(num2)

    elif num1==num3:
        if num4>num2:
            salida.append(num3)
            salida.append(num2)

        if num2>num4:
            salida.append(num3)
            salida.append(num4)

        if num2==num4:
            salida.append(num3)
            salida.append(num2)

    else:
        salida=[]

salida = str(salida).replace(" ", "")
print(salida)
