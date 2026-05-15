import pytest
from Ejemplo2Cuadratica import raices

''' Test para Pytest del Ejemplo 2'''

def test_son_raices():
    assert raices(1, -2, 1) == (1.0, 1.0)  # Raíz doble
    assert raices(1, 2, 5) == "NO hay solución real. Solo raíces complejas"


@pytest.mark.parametrize("a,b,c, esperado", [
    (7, 23, 45, "NO hay solución real. Solo raíces complejas"),
    (1, -3, 2, (2.0, 1.0)),                                     
    (1, -2, 1, (1.0, 1.0)) 
])
def test_raices_param(a, b, c, esperado):
    assert raices(a, b, c) == esperado