import math

# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    
    if figura == "rectángulo":
        
        if len(datos) != 2:
            raise ValueError("El rectángulo necesita base y altura.")
        
        base = datos[0]
        altura = datos[1]
        
        area = base*altura
        
        return area
    
    elif figura == "círculo":
        
        if len(datos) != 1:
            raise ValueError("El círculo necesita un radio.")
        
        radio = datos[0]
        area = math.pi*(radio**2)
        
        return area
    
    elif figura == "triángulo":
        
        if len(datos) != 2:
            raise ValueError("El triángulo necesita base y altura.")
        
        base = datos[0]
        altura = datos[1]
        
        area = (base*altura)/2
        
        return area
        
        
    else:
        raise ValueError ('Figura inválida')  

try:
      
    print(calcular_area("rectángulo", (5, 8)))
    print(calcular_area("círculo", (4,)))
    print(calcular_area("triángulo", (6, 3)))

    print(calcular_area("cuadrado", (5,)))
    
except ValueError as v:
    print(f'Error: {v}')


#Probamos la excepción de parámetros en el círculo como ejempl  
try:
    print(calcular_area("círculo", ()))

except ValueError as v:
    print(f'Error: {v}')