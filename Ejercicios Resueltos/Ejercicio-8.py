#8 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

try:
    numero_uno = int(input('Introduce un número: '))
    numero_dos = int(input ('Introduce otro número: '))
    
    print(f'División exitosa, resultado: {numero_uno/numero_dos}')
    
except ZeroDivisionError:
    print(f'No es posible dividir entre {numero_dos}')
    
except ValueError:
    print('Error. Debes introducir un número')