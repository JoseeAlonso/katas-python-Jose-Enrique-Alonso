# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

def busqueda_nombre():

    lista_nombres = [nombre.strip().lower() for nombre in input('introduce los nombres separados por comas: ').split(',')]
    
    print(lista_nombres)
    
    nombre_busqueda = input('Introduce el nombre a buscar: ').strip().lower()
    
    
    if nombre_busqueda in lista_nombres:
        
        print('¡El nombre ha sido encontrado!')
    
    else:
            
        raise Exception('El nombre que buscas no está en la lista :(')
    
        
try:
    busqueda_nombre()
        
except Exception as e:
        
    print(f'Error: {e}')                

