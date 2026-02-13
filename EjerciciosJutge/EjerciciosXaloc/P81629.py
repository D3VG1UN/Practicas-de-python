#ejercicio 17. cambio

dinero=input()
listanums=dinero.split()
euros=int(listanums[0])
cents=int(listanums[1])
quinientos=0
doscientos=0
cien=0
cincuenta=0
veinte=0
diez=0
cinco=0
dos=0
uno=0
cincuentaCents=0
veinteCents=0
diezCents=0
cincoCents=0
dosCents=0
unCents=0

while euros>0:
    if euros>=500:
        quinientos+=1
        euros-=500
    elif euros>=200 and euros<500:
        doscientos+=1
        euros-=200
    elif euros>=100 and euros<200:
        cien+=1
        euros-=100
    elif euros>=50 and euros<100:
        cincuenta+=1
        euros-=50
    elif euros>=20 and euros<50:
        veinte+=1
        euros-=20
    elif euros>=10 and euros<20:
        diez+=1
        euros-=10
    elif euros>=5 and euros<10:
        cinco+=1
        euros-=5
    elif euros>=2 and euros<5:
        dos+=1
        euros-=2
    elif euros>=1 and euros<2:
        uno+=1
        euros-=1
    else:
        euros=euros

while cents>0:
    if cents>=50:
        cincuentaCents+=1
        cents-=50
    elif cents>=20 and cents<50:
        veinteCents+=1
        cents-=20
    elif cents>=10 and cents<20:
        diezCents+=1
        cents-=10
    elif cents>=5 and cents<10:
        cincoCents+=1
        cents-=5
    elif cents>=2 and cents<5:
        dosCents+=1
        cents-=2
    elif cents>=1:
        unCents+=1
        cents-=1
    else:
        cents=cents

print("Banknotes of 500 euros:",quinientos)
print("Banknotes of 200 euros:",doscientos)
print("Banknotes of 100 euros:",cien)
print("Banknotes of 50 euros:",cincuenta)
print("Banknotes of 20 euros:",veinte)
print("Banknotes of 10 euros:",diez)
print("Banknotes of 5 euros:",cinco)
print("Coins of 2 euros:",dos)
print("Coins of 1 euro:",uno)
print("Coins of 50 cents:",cincuentaCents)
print("Coins of 20 cents:",veinteCents)
print("Coins of 10 cents:",diezCents)
print("Coins of 5 cents:",cincoCents)
print("Coins of 2 cents:",dosCents)
print("Coins of 1 cent:",unCents)