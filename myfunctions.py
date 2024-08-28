def operAritmetic(val1, val2, operator):
    try:
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == '/':
            if val2 == 0:
                raise ValueError("Cannot divide by zero")
            return val1 / val2
        else:
            raise ValueError("Invalid operator")
    except Exception as e:
        print(f"Error: {e}")
        
def calcIva(cifra):
    return cifra * 19/100

# Generar un metodo que permita retornar la cadena los N primeros numeros de la serie
# de fibonacci

# Generar un metodo que permita retornar el factorial de cualquier numero

