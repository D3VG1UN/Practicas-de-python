bacterias_inicio=int(input("Cuantas bacterias había al principio? "))
min_tiempo=int(input("Cuanto tiempo dejamos que se reproduzcan? "))

if min_tiempo>=13:
    veces_reproducen=min_tiempo//13
    bacterias_finales=bacterias_inicio*(2**veces_reproducen)
    print(bacterias_finales)
else:
    print(bacterias_inicio)

