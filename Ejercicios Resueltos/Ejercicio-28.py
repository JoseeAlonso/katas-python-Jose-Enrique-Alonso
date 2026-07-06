# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

palabras = [
    "sol",
    "luna",
    "estrella",
    "mar",
    "sol",
    "árbol",
    "flor",
    "luna",
    "bosque",
    "río",
    "flor",
    "cielo",
    "mar",
    "montaña",
    "sol"
]

def palabra_duplicada(lista):
    
    vistos = set()
    
    for palabra in lista:
        
        if palabra in vistos:
            
            return palabra
        
        vistos.add(palabra)
        
    return None

resultado = palabra_duplicada(palabras)
print(resultado)
    