# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
 
    # Reglas:
    # 0 - 69: insuficiente
    # 70 - 79: bien
    # 80 - 89: muy bien
    # 90 - 100: excelente
     
try:
    
    nota = int(input('Introduce la nota del alumno: '))
    
    if nota >= 0 and nota <=100:
    
        if nota >= 0 and nota < 70:
            print('Insuficiente')
    
        elif nota >= 70 and nota < 80:
            print('Bien')
    
        elif nota >= 80 and nota < 90:
            print('Muy bien')
    
        else:
            print('¡Excelente!')

    else:
        print('Nota inválida. La nota debe estar comprendida entre 0 y 100.')

except ValueError:
    print('Tipo de dato inválido')