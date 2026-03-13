valor=input("Introduce los valores separados por un guion ")
lista_valores=valor.split("-")

lista_nums=[]
lista_texto=[]
lista_decimales=[]
decimal=0
letrasMixtas=0

for i in lista_valores:
    if i.isnumeric():
        lista_nums.append(int(i))
    elif "." in i:
        lista_decimales=i.split(".")
        for n in lista_decimales:
            if n.isnumeric():
                decimal+=1
            else:
                letrasMixtas+=1
        if letrasMixtas>0:
            lista_texto.append(i)
        else:
            lista_nums.append(float(i))
        #con este bucle+condiciones, compruebo que el número introducido no sea una palabra con números dentro
    else:
        lista_texto.append(i)

sumtotal=sum(lista_nums)
lista_nums.sort()
#como menciono más abajo, aqui lo ordeno, siguiento el enunciado, por lo que al final sale ordenado

lista_texto_mayus=[]
for x in lista_texto:
    lista_texto_mayus.append(x.upper())

lista_texto_mayus.sort()

lista_nums_no_duplicados=list(set(lista_nums))
lista_nums_no_duplicados.sort()
lista_texto_no_duplicados=list(set(lista_texto))
lista_mayus_no_duplicados=list(set(lista_texto_mayus))
lista_mayus_no_duplicados.sort()
#set() elimina duplicados, pero no lo convierte en lista - eso ya lo hago yo

sumfinal=sum(lista_nums_no_duplicados)

print("Valores numéricos antes de eliminar duplicados:")
print(lista_nums)
#A pesar del printeo de ejmplo, aquí sale ordenado, porque lo he ordenado antes
print("")
print("Suma total antes de eliminar duplicados:",sumtotal)
print("")
print("Valores numéricos después de eliminar duplicados:",lista_nums_no_duplicados)
print("")
print("Suma total después de eliminar duplicados:",sumfinal)
print("")
print("Valores no numéricos antes de eliminar duplicados:",lista_texto)
print("")
print("Valores no numéricos después de eliminar duplicados:",lista_mayus_no_duplicados)
