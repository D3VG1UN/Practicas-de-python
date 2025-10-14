frase=input("Introduce una frase: ")
num1=float(input("Introduce un número real: "))
num2=float(input("Introduce otro número real: "))
num3=float(input("Introduce otro número real: "))

frase=frase.strip()
frase=frase.lower()
suma=num1+num2+num3
media=round((num1+num2+num3)/3, 2)
producto=num1*num2*num3

print("Frase en minúsculas:",frase)
print("La suma es:",suma)
print("La media es:",media)
print("El producto es:",producto)

if suma>producto:
    print("¿La suma es mayor que el producto? True")
elif suma<producto or suma==producto:
    print("¿La suma es mayor que el producto? False")
