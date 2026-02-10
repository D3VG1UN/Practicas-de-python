#ejercicio3. sumas

num1=input()
if " " in num1:
    listanum=num1.split()
    print(int(listanum[0]) + int(listanum[1]))
else:
    num2=input()
    print(int(num1)+int(num2))