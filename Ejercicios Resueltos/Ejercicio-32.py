# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

empleados = [
    {"nombre": "Ana García", "puesto": "Programadora"},
    {"nombre": "Pedro López", "puesto": "Diseñador"},
    {"nombre": "María Pérez", "puesto": "Gerente"}
]

def busqueda_empleado(nombre_completo, lista_empleados):
    
    for empleado in lista_empleados:
        
        if empleado['nombre'] == nombre_completo:
            
            return f'¡Excelente! El nombre ha sido encontrado y tiene como puesto {empleado["puesto"]}'
            
    return 'La persona a buscar no trabaja en la empresa'   

resultado = busqueda_empleado('Ana García', empleados)
print(resultado)     