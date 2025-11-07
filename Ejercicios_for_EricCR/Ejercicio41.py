#Imprime el siguiente patrón utilizando for
# 54321
#4321
#321
#21
#1

num=54321
for i in range (5):
    if num>60000:
        num=num-50000
        print(num)
    elif num>6000:
        num=num-4000
        print(num)
    elif num>600:
        num=num-300
        print(num)
    elif num>60:
        num=num-20
        print(num)