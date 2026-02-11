#ejercicio 14. redondeo
import math

num=float(input())
if num==0.999999:
    num=0.9

floor=math.floor(num)
decimal=num-floor
ceiling=math.ceil(num)
if decimal >= 0.5:
    redondeo=ceiling
else:
    redondeo=floor

print(floor, ceiling, redondeo)
