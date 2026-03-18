def elegir_operacion(tipo):
    """Retorna una función según el tipo de operación"""

    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    if tipo == "suma":
        return sumar
    elif tipo == "resta":
        return restar

# Obtener la función deseada
operacion = elegir_operacion(input())
resultado = operacion(10, 5)
print(resultado)  # 15
