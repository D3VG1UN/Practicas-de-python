#ejercicio 18. años bisiestos

ano=input()
siglasprimeras=ano[0]+ano[1]
bisiesto=""

if int(ano)%4==0:
    if ano[2]=="0" and ano[3]=="0":
        if int(siglasprimeras)%4==0:
            bisiesto="YES"
        else:
            bisiesto="NO"
    else:
        bisiesto="YES"
else:
    bisiesto="NO"

print(bisiesto)
