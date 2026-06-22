#1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

#Para ejecutar esto con el input, se debe ejecutar el archivo .py desde la terminal. Para usarlo con "Run Code", se puede quitar el input y declarar una cadena de texto predeterminada. ¡Muy importante! GUARDAR LOS CAMBIOS con CTRL+S

cadena_texto = input('Introduce una oración o palabra: ')

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