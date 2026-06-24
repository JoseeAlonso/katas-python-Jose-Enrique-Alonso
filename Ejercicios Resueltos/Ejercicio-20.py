#20 Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

mi_lista = [10, "Hola", 25, "Mundo", 100, "Python"]

resultado = list(filter(lambda elemento: isinstance(elemento,int), mi_lista))

print(resultado)