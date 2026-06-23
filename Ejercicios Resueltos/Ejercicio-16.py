#16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

texto = 'Esto es un texto donde podremos verificar si la función que hemos creado está correcta o no'

def palabras_largas (texto, numero):
    
    palabras = texto.split()
    
    return list(filter(lambda palabra: len(palabra) > numero, palabras))

resultado = palabras_largas(texto,4)
print(resultado)