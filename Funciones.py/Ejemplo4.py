# Correcto
def funcion(param_obligatorio, param_opcional="valor"):
    pass

# Incorrecto - SyntaxError
def funcion(param_opcional="valor"):
    pass
#aqui no aparece, pero si pones param_obligatorio (u otra variable sin definir) como segundo valor, muestra error