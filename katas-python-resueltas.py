import random

#1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

#Para ejecutar esto con el input, se debe ejecutar el archivo .py desde la terminal. Para usarlo con "Run Code", se puede quitar el input y declarar una cadena de texto predeterminada. ¡Muy importante! GUARDAR LOS CAMBIOS con CTRL+S

cadena_texto = input('Introduce una oración o palabra')

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

def lista_doble (num):
    return num*2

numeros = [1,2,3,4,5,6,7,8,9]

resultado_map = map(lista_doble,numeros)

print(f'El resultado de la ejecución de la función map es : {resultado_map}')

lista_resultado = list(map(lista_doble,numeros))

print(f'El resultado despues de convertirlo a una lista es: {lista_resultado}')

#Observación del ejercicio anterior: leyendo un poco más en el temario sobre las distintas posibilidades de hacer este ejercicio, es posible hacerlo con la función lambda, sin embargo lo dejaré de la forma básica que fue la primera que hice.


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


#4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

#Realicé el ejercicio utilizando función lambda y la función abs para devolver un valor absoluto. Imprimo también las listas aleatorias para que se peuda confirmar que la diferencia es la correcta.

lista_uno = [random.randint(1,100) for _ in range(6)]
lista_dos = [random.randint(1,100) for _ in range(6)]

print(f'La lista uno contiene los valores\n {lista_uno}, \nla lista dos contiene los valores\n {lista_dos}')

resultado_map_2 = list(map(lambda a,b: abs(a-b), lista_uno, lista_dos))
    
print(f'La diferencia entre los valores es: {resultado_map_2}')