#7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

lista_tupla = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0)]

def conversion (lista_tupla):
    
    resultado = list(map(lambda tupla: str(tupla), lista_tupla))
    
    #Esto se puede simplificar de esta manera: resultado = list(map(str, lista_tupla)); str ya es una función por sí sola.
    
    return resultado 
    
print(conversion(lista_tupla))