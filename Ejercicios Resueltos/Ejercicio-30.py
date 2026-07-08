# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

#En este ejercicio ordené las letras de cada palabra por orden alfabético para ver si coinciden. Sin embargo, es posible incluir una excepción por si ambas palabras son la misma, no permita hacer la comparación.

def anagramas (palabra1, palabra2):
    
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    return sorted(palabra1) == sorted(palabra2)

resultado = anagramas('hola','adios')
# resultado = anagramas('amor','roma')

print(f'¿La palabra es un anagrama?: {resultado}')