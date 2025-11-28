#actividad 3. Introducir cifras, número, y que sume las cifras y presente el total por pantalla

cifras=int(input("Introduce la cantidad de cifras: "))
num=input("Introduce el número que respete las cifras introducidas: ")
sumacifras=0

#la dificultad aquí es principalmente el cambio de "unidades". Iba a hacer que num fuese int, pero al ver que lo necesito más como string
#que como int he decidido cambiarlo
if cifras==len(num):
    for i in range (cifras):
        #hacemos un valor númerico cada posición del número (como he dicho antes, string).
        sumacifras+=int(num[i])
        #he decidido hacerlo sin el formato (f) porque es corto e innecesario.
    print("Resultado:",sumacifras)
else:
    print("Error, no coincide el número de cifras")