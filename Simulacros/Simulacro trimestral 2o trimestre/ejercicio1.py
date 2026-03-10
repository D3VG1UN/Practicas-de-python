nums=input().split(",")
lista_nums=[]
for i in range (len(nums)):
    lista_nums.append(nums[i])

lista_nums=[int(x) for x in lista_nums]
#lista_nums=list(map(int, lista_nums))

#la función "map" la aprendí en el concurso y ayuda a convertir
#todos los valores en un mismo tipo de variable, pero he decidio usar la otra manera

print(nums)
lista_nums.sort()
lista_nums.remove(lista_nums[0])
lista_nums.remove(lista_nums[int(len(lista_nums))-1])
print(lista_nums)
media=round(sum(lista_nums)/int(len(lista_nums)),2)

print(media)

if media<5:
    print("Rendimiento bajo")
elif media>=5 and media<=10:
    print("Rendimiento medio")
else:
    print("Rendimiento alto")