import random

#4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

#Realicé el ejercicio utilizando función lambda y la función abs para devolver un valor absoluto. Imprimo también las listas aleatorias para que se peuda confirmar que la diferencia es la correcta.

lista_uno = [random.randint(1,100) for _ in range(6)]
lista_dos = [random.randint(1,100) for _ in range(6)]

print(f'La lista uno contiene los valores\n {lista_uno}, \nla lista dos contiene los valores\n {lista_dos}')

resultado_map_2 = list(map(lambda a,b: abs(a-b), lista_uno, lista_dos))
    
print(f'La diferencia entre los valores es: {resultado_map_2}')