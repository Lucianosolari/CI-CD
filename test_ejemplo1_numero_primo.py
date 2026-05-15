import pytest
from Ejemplo1NumeroPrimo import esPrimo

''' Test para Pytest del Ejemplo 1'''

def test_es_primo():
    assert esPrimo(3) is True
    assert esPrimo(2) is True
    assert esPrimo(8) is False
    assert esPrimo(1) is False

@pytest.mark.parametrize("numero, esperado", [
    (7, True),
    (37, True),
    (17, True),
    (20, False),
    (0, False),
    (38, False)
])
def test_es_primo_param(numero, esperado):
    assert esPrimo(numero) == esperado