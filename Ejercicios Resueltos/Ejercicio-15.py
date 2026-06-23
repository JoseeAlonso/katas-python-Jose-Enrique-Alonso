#15 Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [10, 23, 45, 67, 89, 12, 34, 56, 78, 90]

lambda_sumar_3 = lambda lista: [numero + 3 for numero in lista]

#También se peude hacer: lambda_sumar_3 = lambda lista: list(map(lambda numero: numero + 3, lista))

resultado = lambda_sumar_3(numeros)
print(resultado)