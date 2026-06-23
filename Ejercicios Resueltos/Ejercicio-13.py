#13 Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

#Observación: Tuve que buscar un poco de ayuda para este ejercicio ya que no entendía exactamente que se requería. Estaba haciendo un for en una palabra pero no era lo que se pedía y me quedé un poco atascado :')

def funcion_espejo(palabra):
    
    return list(map(lambda letra: (letra.upper(), letra.lower()), sorted(palabra)))

conjunto_caracteres = {'a','b','c','d','e'}

resultado = funcion_espejo(conjunto_caracteres)
print(resultado)
        