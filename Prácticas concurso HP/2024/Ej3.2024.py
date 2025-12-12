atomosC=int(input("Introduce los átomos de carbono: "))
atomosH=(atomosC*2)+2
peso=atomosC*12+atomosH
masaNombre="C"+str(atomosC)+"H"+str(atomosH)

print(f"La masa atómica de {masaNombre} es {peso}")