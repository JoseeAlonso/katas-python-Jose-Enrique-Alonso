#9 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

animales_excluidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

lista_animales = ['Delfín', 'Tigre', 'Perro', 'Gato', 'Mapache', 'Serpiente Pitón', 'Ornitorrinco', 'Mamut', 'Cocodrilo', 'Oso', 'Ciervo', 'Orca']


def filtrar_lista (lista_mascotas):
    
    return list(filter(lambda mascota: mascota not in animales_excluidos, lista_mascotas))


resultado = filtrar_lista(lista_animales)

print(resultado)