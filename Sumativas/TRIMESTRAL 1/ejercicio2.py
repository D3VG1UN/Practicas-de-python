#actividad 2. Introducir 6 números por teclado y se sumen los positivos, los negativos y se muestren por pantalla

sumanegativos=0
sumapositivos=0

for i in range (0, 6):
    num=int(input("Introduce un valor: "))
    #comprobación simple si es mayor o igual a 0 (positivo). En caso contrario, será negativo.
    if num>=0:
        sumapositivos+=num
    else:
        sumanegativos+=num

print(f"Suma de números positivos: {sumapositivos}")
print(f"Suma de números negativos: {sumanegativos}")
