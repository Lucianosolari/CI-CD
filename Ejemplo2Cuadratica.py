''' Ejemplo 2: 
Una función que, dado el ingreso de 3 variables (a, b, c), retorne las raíces 
resultantes de una ecuación cuadrática.
'''
def raices(a,b,c):
    """
    Calcula las raíces de una ecuación cuadrática ax**2 + bx + c = 0
    Ingresan las variables a,b y c. 
    Retorna una tupla si tiene raices reales o ambas raices son el mismo número solo si el discriminante
    es mayor o igual a cero. En cambio si a es 0 o el discriminante es menor que cero retorna un string.
    """
    if a==0:
        raise ValueError("El coeficiente 'a' no puede ser 0. NO es una ecuación cuadrática")
    
    discriminante=(b**2)-4*a*c
    if discriminante <0:
        return "NO hay solución real. Solo raíces complejas"
    elif discriminante >=0: #agrego =0 porque es lo mismo, la raiz de ambas es el mismo número.
        discriminante = discriminante**0.5
        raiz1=(-b+discriminante)/(2*a)
        raiz2=(-b-discriminante)/(2*a)
        return raiz1, raiz2

'''
#Ejemplo para verificar el código
x1, x2 = raices(1, -2, 1)
print(f"x1 = {x1}, x2 = {x2}")

resultado = raices(1, 2, 5)
print(resultado)
'''