def saludar(nombre, saludo="Hola"):
    """Saluda a una persona con un saludo personalizable"""
    return f"{saludo}, {nombre}!"

print(saludar("María"))  # Hola, María!
print(saludar("Pedro", "Buenos días"))  # Buenos días, Pedro!
print(saludar("Mario", saludo="Digamelón"))  # Qué tal, Ana!