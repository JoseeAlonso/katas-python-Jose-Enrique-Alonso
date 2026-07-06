from functools import reduce
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().

numeros = [100, 20, 15, 5, 10]

resultado = reduce(lambda acumulador, numero: acumulador - numero, numeros)
print(f'La diferencia de los valores de la lista es: {resultado}')