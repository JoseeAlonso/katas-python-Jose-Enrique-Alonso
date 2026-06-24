#18 Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [{
    'nombre': 'Jose',
    'edad': 30,
    'calificación': 89}
,{
    'nombre': 'Maria',
    'edad': 25,
    'calificación': 69}
,{
    'nombre': 'Adriana',
    'edad': 29,
    'calificación': 100}
,{
    'nombre': 'Ernesto',
    'edad': 54,
    'calificación': 90}
]

# Se puede hacer con un lambda, pero visualmente me gusta verlo de la manera "def".Quedaría así: resultado = list(filter(lambda estudiante: estudiante['calificación] >= 90, estudiantes))

def sobresalientes (estudiante):
    
    return estudiante['calificación'] >= 90

resultado = list(filter(sobresalientes, estudiantes))
print(resultado)
        