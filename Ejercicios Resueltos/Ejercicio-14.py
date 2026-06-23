#14 Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

def retorno_lista (lista, letra):
    letra = letra.lower()
    return list(filter(lambda palabra : palabra.lower().startswith(letra), lista))

palabras = [
    "árbol", "arena", "azul", "almohada", "agua",
    "barco", "blanco", "bosque", "bici", "botella",
    "casa", "cielo", "carro", "computadora", "comida",
    "dado", "dedo", "diente", "dinero", "dormir",
    "espejo", "estrella", "escuela", "elefante", "escritorio",
    "fuego", "flor", "fruta", "fácil", "foto",
    "gato", "guitarra", "globo", "galleta", "grande",
    "hielo", "hoja", "hilo", "huevo", "hermano",
    "isla", "imán", "idea", "iglesia", "invierno",
    "jardín", "jugo", "juguete", "joven", "jirafa"
]

resultado = retorno_lista(palabras, "C")
print(resultado)