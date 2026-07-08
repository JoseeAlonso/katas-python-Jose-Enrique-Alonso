# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = list(map(lambda numeroX, numeroY: numeroX + numeroY,lista1, lista2))

print(resultado)