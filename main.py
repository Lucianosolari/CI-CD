def suma(a, b):
    return a + b

def potencia(a, b):
    return a ** b 

def resta(a, b):
    return a - b


def multiplica(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def isString(value):
    return value.isalpha()

def isPar(n):
    return n % 2 == 0

def mayor(a, b):
    return a if a > b else b
def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return n ** 0.5
