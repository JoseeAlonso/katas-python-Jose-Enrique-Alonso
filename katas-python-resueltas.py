#1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

#Para ejecutar esto con el input, se debe ejecutar el archivo .py desde la terminal. Para usarlo con "Run Code", se puede quitar el input y declarar una cadena de texto predeterminada. ¡Muy importante! GUARDAR LOS CAMBIOS con CTRL+S

cadena_texto = input("Introduce una oracion o palabra")

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



#2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

#Importante el pasar a lista el resultado ya que lo que arroja el map() es un object.

def funcion (num):
    return num*2

numeros = [1,2,3,4,5,6,7,8,9]

resultado_map = map(funcion,numeros)

print(f'El resultado de la ejecución de la función map es : {resultado_map}')

lista_resultado = list(map(funcion,numeros))

print(f'El resultado despues de convertirlo a lista es: {lista_resultado}')
