def operation_selector(num1, num2, op):
    # Función que llama 2 variables int y una variable string
    # Realiza operación de 2 números con operando
    if (not isinstance(num1, int) or not isinstance(num2, int) or
            isinstance(num1, bool) or isinstance(num2, bool)):
        # Revisa que num1 y num 2 sean números enteros, y no hayan booleanos
        return (-50, None)
        # Código de error -50 para valores no enteros

    if not isinstance(op, str):  # Revisa que op sea de tipo string
        return (-60, None)
        # Si no es string, código de error -60 para valores no string

    if op not in ['+', '-', '*', '&']:
        # Revisa que op sea una operación válida
        return (-70, None)
        # Código de error -70 para operación invalida

    if op == "+":  # Verifica operando de suma
        result = num1 + num2  # Realiza suma
    elif op == "-":  # Verifica operando de resta
        result = num1 - num2  # Realiza resta
    elif op == "*":  # Verifica operando de multiplicación
        result = num1 * num2  # Realiza multiplicación
    elif op == "&":  # Verifica operando de lógica
        result = num1 & num2  # Realiza lógica

    return (0, result)  # Retorna código de éxito 0 y resultado.


def calculo_promedio(lista_valores):
    # Función que llama una lista de números
    # Se obtiene promedio de una lista de números
    if (not all(isinstance(i, (int, float)) for i in lista_valores)
            or any(isinstance(i, bool) for i in lista_valores)):
        # Verifica que la lista contenga valores int o float
        # No permite valores bool
        return (-80, None)
        # Código de error -80 para valores no números

    if len(lista_valores) > 10:
        # Verifica que la lista no sea mayor de 10 valores
        return (-90, None)
        # Código de error -90 por poseer más de 10 elementos

    promedio = sum(lista_valores) / len(lista_valores)  # Operación promedio
    return (0, promedio)  # Retorna código de éxito y promedio
