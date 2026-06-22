import random

#5 Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

notas = [random.randint(1,10) for _ in range(5)]

def evaluacion_notas (notas, nota_aprobado):
    
    total_notas = 0
    
    for nota in notas:
        total_notas += nota 
        
    media = total_notas/(len(notas))
    
    #Esto se puede acortar de esta manera: media = sum(notas) / len(notas), sin embargo, hago los ejercicios tratando de entender siempre la lógica de cada paso.
    
    if media >= nota_aprobado:
        estado = 'Aprobado'
    else:
        estado = 'Suspenso'
            
    return (media, estado)

resultado = evaluacion_notas(notas, 5)

print(f'Notas: {notas}')
print(f'Media: {resultado}')