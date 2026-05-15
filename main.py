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

def factorial(n):
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado