# Crea una función que calcule el promedio de una lista de números.

numeros = [12, 7, 25, 3, 18, 40, 9, 15, 27, 6]

def promedio_lista(lista):
    return sum(lista)/len(lista)

resultado = promedio_lista(numeros)
print(resultado)