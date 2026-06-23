from functools import reduce

#17 Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

lista_digitos = [5,7,2,6,8] 

def funcion_digitos (lista):
    
    return reduce(lambda acumulador, digito: acumulador * 10 + digito, lista)

resultado = funcion_digitos(lista_digitos)
print(resultado)