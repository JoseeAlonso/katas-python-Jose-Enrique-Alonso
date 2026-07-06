from functools import reduce
# Concatena una lista de palabras. Usa la función reduce().

palabras = [
    "sol",
    "luna",
    "estrella",
    "cielo",
    "mar",
    "montaña",
    "río",
    "árbol",
    "flor",
    "bosque"
]

resultado = reduce(lambda acumulador, elemento: acumulador+' '+elemento, palabras)
print(resultado)