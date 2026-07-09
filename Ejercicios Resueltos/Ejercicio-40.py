# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:

    #a. Solicitar al usuario el precio original de un artículo.
    #b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    #c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    #d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    #e. Mostrar el precio final de la compra, considerando o no el descuento.
    #f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

try:
    
    precio_original = float(input('Introduce el precio original del producto '))

    tiene_cupon = input('¿Tienes cupón de descuento? ').strip().lower()

    if tiene_cupon == "si":
    
        valor_descuento = float(input('Introduce el valor del descuento '))
    
        if 0 < valor_descuento <= precio_original:
        
            precio_producto = precio_original-valor_descuento
        
            print(f'El precio final del producto con el descuento sería de {precio_producto}')
        
        else:
            print('El cupón no es válido. El descuento debe ser mayor que 0 y no superar el precio del producto.')
        
    elif tiene_cupon == "no":
        print(f'El precio final de producto sería {precio_original}')
        
    else:
        print('Respuesta inválida. Debes responder "si" o "no".')
        
except ValueError:
    print('Error: debes introducir un número válido')
    
#Para este ejercicio, la política de la empresa es que si el valor del descuento es mayor al precio original del producto, el cupón se considera inválido. Existe la opción de si el descuento es mayor al precio original, el precio de compra = 0€. TODO DEPENDE DE LAS POLÍTICAS DE LA EMPRESA.