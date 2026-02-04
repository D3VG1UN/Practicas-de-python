#ejercicio 4. suma3

num1=input()

if " " in num1:
    listanums=num1.split()
    print(int(listanums[0])+int(listanums[1])+int(listanums[2]))
else:
    num1.strip()
    listanums=num1.split()
    num2=input()
    print(int(listanums[0])+int(listanums[1])+num2)
