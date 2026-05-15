''' Ejemplo 1: 
Un programa que dado el ingreso de un número retorne si el mismo es 
primo o no.
'''
def esPrimo(num):
    """
    Evalua si un número es primo o no
    Ingresan una sola variable: número 
    Retorna True si es primo o False en caso contrario.
    """
    if num<=1:
        return False
    
    contador=0;
    for i in range (2,num+1):
        if num%i==0:
            contador+=1
    if contador>1:
        return False
    else:
        return True

'''   
#Ejemplo# para verificar el código ingresando por el usuario
numero = int(input("Ingrese un número: "))#Se puede probar con 7 o 37, que son primos
print("Es un número primo" if esPrimo(numero) else "NO es un número primo")

'''