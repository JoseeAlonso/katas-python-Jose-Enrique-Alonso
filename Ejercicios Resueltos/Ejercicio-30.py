# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagramas (palabra1, palabra2):
    
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    return sorted(palabra1) == sorted(palabra2)

resultado = anagramas('hola','adios')
# resultado = anagramas('amor','roma')

print(f'¿La palabra es un anagrama?: {resultado}')