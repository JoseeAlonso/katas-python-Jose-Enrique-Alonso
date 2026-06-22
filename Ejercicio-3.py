#3 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def lista_objetivo(lista_palabras, palabra_objetivo):
    
    resultado = []
    palabras_encontradas = 0
    
    for palabra in lista_palabras:
        
        if palabra_objetivo.lower() in palabra.lower():
            
            palabras_encontradas += 1
            
            resultado.append(palabra)
            
    print(f'La palabra {palabra_objetivo} se encuentra {palabras_encontradas} veces y la lista es {resultado}')
    
    return resultado

lista_palabras = ['Azul', 'Rojo', 'Verde', 'Amarillo', 'Celeste', 'Morado', 'Verde', 'Verde']

palabra_objetivo = input('Introduce la palabra a buscar: ')

lista_objetivo(lista_palabras, palabra_objetivo)