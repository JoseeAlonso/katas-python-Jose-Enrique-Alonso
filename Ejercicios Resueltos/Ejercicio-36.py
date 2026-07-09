'''
Crea una función llamada procesar_texto

Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.

Código a seguir:
Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.

Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.

Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.

Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

Caso de uso:
Verificar el funcionamiento completo de procesar_texto.
'''

def contar_palabras(texto):
    palabras = texto.split()
    
    contador_palabras = {}
    
    for palabra in palabras:
        
        if palabra in contador_palabras:
            
            contador_palabras[palabra] += 1

        else:
            contador_palabras[palabra] = 1
            
    return contador_palabras   

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    
    return texto.replace(palabra, '')

    # También se puede hacer de esta manera y evitar el espaciado que genera replace() al hacerlo de esa forma:
    # return " ".join([p for p in texto.split() if p != palabra])

def procesar_texto(texto, opcion, *args):
    
    if opcion == "contar":
        return contar_palabras(texto)
        
    elif opcion  == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
        
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    
    else:
        raise ValueError('Opción no válida')

texto = "hola Madrid hola Antonio Madrid"
    
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "hola", "adiós"))
print(procesar_texto(texto,"eliminar", "Madrid"))