# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def funcion_enmascarar(elemento):
    
    texto = str(elemento)
    
    return '#' * (len(texto) - 4) + texto[-4:]
        
resultado = funcion_enmascarar(1234567890)
print(resultado)    
