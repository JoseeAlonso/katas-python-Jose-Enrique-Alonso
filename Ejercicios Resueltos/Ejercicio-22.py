from functools import reduce

#22 Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = reduce(lambda acumulador, numero: acumulador*numero, lista_numeros)
print(resultado)