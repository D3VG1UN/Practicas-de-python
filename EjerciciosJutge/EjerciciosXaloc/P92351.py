# ejercicio 10. división por num natural

num=input()
nums=num.split()
b=int(nums[1])
a=int(nums[0])

if b == 0:
    print("Please, b cannot be 0")
else:
    d=a//b
    r=a%b
    print(d, r)