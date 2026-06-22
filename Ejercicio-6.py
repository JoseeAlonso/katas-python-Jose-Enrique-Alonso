import random

#6 Escribe una función que calcule el factorial de un número de manera recursiva.

numero = random.randint(1, 10)

def factorial (n):
    
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'El factorial de {numero} es {factorial(numero)}')