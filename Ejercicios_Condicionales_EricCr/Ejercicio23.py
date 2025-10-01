#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota=float(input("Introduce tu nota entre 1 y 10: "))

if nota<0 or nota>10:
    print("¿No te he dicho que esté entre 1 y 10?")
else:
    if nota<5:
        print(f"Has sacado un {nota}, que es un insuficiente")
    elif nota<6.5>=5:
        print(f"Has sacado un {nota}, que es un satisfactorio")
    elif nota<8.5>=6.5:
        print(f"Has sacado un {nota}, que es un notable")
    elif nota<=10>8.5:
        print(f"Has sacado un {nota}, que es un excelente")