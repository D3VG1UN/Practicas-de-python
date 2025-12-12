#CodeWars

ano=int(input("Introduce un año: "))
edicion=ano-2015

if ano <= 2025 and ano >= 2015 and not ano==2020:
    print(f"La edición es: {edicion}")
elif ano == 2020:
    print("CANCELADA")
elif ano > 2025:
    print("Próximamente")
elif ano < 2015:
    print("No existía")