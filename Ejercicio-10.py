import random

#10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

numeros = [random.randint(1,100) for _ in range(8)]
# Podemos utilizar numeros = [] para verificar si arroja el error cuando la lsita está vacía.

class ExcepcionPersonalizada(Exception):
    pass
 

def promedio_lista (lista):
    
    if len(lista) == 0:
        
        raise ExcepcionPersonalizada('La lista no puede estar vacía')
    
    media = sum(lista) / len(lista)
    return media

try:
    resultado = promedio_lista(numeros)
    
    print(f'El promedio es: {resultado:.2f}')
    
except ExcepcionPersonalizada as e:
    print(f'Error: {e}')
    