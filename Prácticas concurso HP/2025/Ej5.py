golesO=(input("Goles de Oliver: "))
golesM=(input("Goles de Mark: "))
golesO=golesO.split()
golesM=golesM.split()

Omas=0

for i in range (len(golesO)):
    if int(golesO[i]) > int(golesM[i]):
        Omas+=1
    else:
        Omas=Omas
print(Omas)