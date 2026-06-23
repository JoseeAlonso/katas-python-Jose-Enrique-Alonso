#11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

class ExcepcionPersonalizada(Exception):
    pass

def validador_edad (edad):
    
    if edad < 0 or edad > 120:
            
        raise ExcepcionPersonalizada('Valores fuera de los permitidos. La edad debe estar entre 0 y 120 años')
        
    print('¡Edad correcta!')    
    
    
try:
        
        edad = int(input('Introduce tu edad: '))
        validador_edad(edad)
        
except ValueError:
        print('Valores no permitidos. Debes introducir un número.')
        
except ExcepcionPersonalizada as e:
        print(f'Error: {e}')    
        
