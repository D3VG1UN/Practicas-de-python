variable=input("valores: ").split(",")
lista=[int(x) for x in variable]

#join - mirarselo (de lista a texto)

print(lista)
valormax=max(lista)
valormin=min(lista)

lista.remove(valormax)
lista.remove(valormin)

valormedia=round(sum(lista)/len(lista),2)
print("La media es:",valormedia)

if valormedia<5:
    print("Rendimiento bajo")
elif valormedia>=5 and valormedia<=10:
    print('Rendimiento medio')
else:
    print("Rendimiento alto") 