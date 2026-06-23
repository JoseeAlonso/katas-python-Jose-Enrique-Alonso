#12 Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras (frase):
    
    return list(map(lambda palabra: len(palabra), frase.split()))

frase = input('Introduce una frase: ')
print(longitud_palabras(frase))