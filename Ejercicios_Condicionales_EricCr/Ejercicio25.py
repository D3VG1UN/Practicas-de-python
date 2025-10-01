#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

nota=float(input("Introduce tu nota entre 1 y 10: "))


if nota<5:
        print(f"Has sacado un {nota}, que es un insuficiente")
elif nota<6.5 and nota>=5:
        print(f"Has sacado un {nota}, que es un satisfactorio")
elif nota<8.5 and nota>=6.5:
        print(f"Has sacado un {nota}, que es un notable")
elif nota<=10 and nota>8.5:
        print(f"Has sacado un {nota}, que es un excelente")
else:
    print("¿No he dicho que esté entre 1 y 10?")