#2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

#Importante el pasar a lista el resultado ya que lo que arroja el map() es un object.

def lista_doble (num):
    return num*2

numeros = [1,2,3,4,5,6,7,8,9]

resultado_map = map(lista_doble,numeros)

print(f'El resultado de la ejecución de la función map es : {resultado_map}')

lista_resultado = list(map(lista_doble,numeros))

print(f'El resultado despues de convertirlo a una lista es: {lista_resultado}')

#Observación del ejercicio: leyendo un poco más en el temario sobre las distintas posibilidades de hacer este ejercicio, es posible hacerlo con la función lambda, sin embargo lo dejaré de la forma básica que fue la primera que hice.