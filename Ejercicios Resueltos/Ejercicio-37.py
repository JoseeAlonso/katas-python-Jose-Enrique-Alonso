from datetime import datetime, time

# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

hora_usuario = input('Introduce una hora (Formato HH:MM): ')

try:
    hora = datetime.strptime(hora_usuario, "%H:%M").time()
    
    if time(6, 0) <= hora < time(12, 0):
        print('¡Es de día!')
        
    elif time(12, 0) <= hora < time(20, 0):
        print('¡Es de tarde!')
        
    else:
        print('¡Es de noche!')
        
except ValueError:
    print('Formato de hora no válido.')