#1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

cadena_texto = input(f'Introduce una oracion o palabra:')

def frecuencia_letras (cadena_texto):
    frecuencias = {}
    
    for letra in cadena_texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] +=1
            else:
                frecuencias[letra] = 1
                
    return frecuencias

resultado = frecuencia_letras(cadena_texto)

print(resultado)