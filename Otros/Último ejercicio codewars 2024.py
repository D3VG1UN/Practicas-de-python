import sys

ADVANTAGE = 0
NEUTRAL = 1
DISADVANTAGE = 2

ELEMENT = 0
RACE = 1

DRAGON = 0
DEMON = 1
GOLEM = 2
TROLL = 3

# Número de turnos por monstruo según ventaja/neutral/desventaja
MONSTER_TURNS = [
    [7, 9, 12],  # DRAGON
    [3, 7, 11],  # DEMON
    [2, 5, 7],   # GOLEM
    [2, 3, 5]    # TROLL
]

# Elementos en orden de preferencia
ELEMENTS = ["Fire", "Ice", "Earth"]


def calcSpentTurns(currentMonster, playerElement):
    monsterElement = currentMonster[ELEMENT]

    # Determinar ventaja / desventaja / neutral
    if playerElement == monsterElement:
        strategy = NEUTRAL
    else:
        if monsterElement == "Fire":
            strategy = ADVANTAGE if playerElement == "Earth" else DISADVANTAGE
        elif monsterElement == "Ice":
            strategy = ADVANTAGE if playerElement == "Fire" else DISADVANTAGE
        else:  # Earth
            strategy = ADVANTAGE if playerElement == "Ice" else DISADVANTAGE

    # Determinar la raza
    race = currentMonster[RACE]

    if race == "Dragon":
        return MONSTER_TURNS[DRAGON][strategy]
    elif race == "Demon":
        return MONSTER_TURNS[DEMON][strategy]
    elif race == "Golem":
        return MONSTER_TURNS[GOLEM][strategy]
    else:
        return MONSTER_TURNS[TROLL][strategy]


def printFinalCombination(monsters, turnEquipmentChange, initialElement, elementChange):
    print("Initial equipment: " + initialElement)

    for i in range(len(monsters)):
        if i == turnEquipmentChange and elementChange != initialElement:
            print("Changing to " + elementChange + " equipment")

        print(monsters[i][ELEMENT] + " " + monsters[i][RACE])


###################### MAIN ######################

lowestTurnCount = sys.maxsize
finalPosTurnChange = sys.maxsize

monsters = []

numMonsters = int(input())

# Leer monstruos
for _ in range(numMonsters):
    monsterData = input().split()
    monsters.append(monsterData)

# Probar los 3 elementos iniciales posibles
for initialElementIndex in range(3):

    # Probar todos los puntos posibles para cambiar equipo
    for currentChange in range(numMonsters):

        # Calcular el primer monstruo
        turnSum = calcSpentTurns(monsters[0], ELEMENTS[initialElementIndex])

        # Sumar turnos hasta el punto de cambio
        for currentMonster in range(1, currentChange):
            turnSum += calcSpentTurns(monsters[currentMonster], ELEMENTS[initialElementIndex])

        # Probar los 3 elementos posibles para el cambio
        for newElementIndex in range(3):

            if newElementIndex != initialElementIndex:
                turnSumNewElement = turnSum + 2  # Cambiar equipo cuesta 2 turnos
            else:
                turnSumNewElement = turnSum

            # Calcular turnos desde el cambio en adelante
            for currentMonster in range(currentChange, numMonsters):
                turnSumNewElement += calcSpentTurns(monsters[currentMonster], ELEMENTS[newElementIndex])

            # Si es la mejor combinación, guardarla
            if turnSumNewElement < lowestTurnCount:
                lowestTurnCount = turnSumNewElement
                finalPosTurnChange = currentChange
                finalInitialElement = ELEMENTS[initialElementIndex]
                finalElementChange = ELEMENTS[newElementIndex]

# Imprimir salida
printFinalCombination(monsters, finalPosTurnChange, finalInitialElement, finalElementChange)
