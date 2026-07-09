'''
Crea la clase UsuarioBanco

Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.

Métodos: retirar_dinero, transferir_dinero, agregar_dinero.

Código a seguir:

Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.

Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.

Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.

Implementar agregar_dinero para aumentar el saldo del usuario.

Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.
'''

class UsuarioBanco:
    
    def __init__(self,nombre, saldo, tieneCuentaCorriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tieneCuentaCorriente = tieneCuentaCorriente
        
    def retirar_dinero(self, monto):
        
        if monto > self.saldo:
                
            raise Exception (f'Imposible retirar esa cantidad, su saldo es insuficiente. Saldo actual: {self.saldo}')
                
        self.saldo -= monto
                
    def transferir_dinero (self, usuario_destino, monto):
        
        self.retirar_dinero(monto)
        usuario_destino.agregar_dinero(monto)
        
    def agregar_dinero(self, monto):
        
        self.saldo += monto
    
    def mostrar_info(self):
        
        return f'El nombre del usuario es {self.nombre} y el saldo actual es de {self.saldo}'
    

#Creamos dos usuarios
alicia = UsuarioBanco('Alicia', 100, True)
bob = UsuarioBanco('Bob', 50, True)

#Agregar 20 unidades a Bob
bob.agregar_dinero(20)

#Transferir 80 unidades desde Bob a Alicia
try:
    bob.transferir_dinero(alicia, 80)
    
except Exception as e:
    print(f'Error: {e}')  

#Retirar 50 undiades de saldo de Alicia
try:
    alicia.retirar_dinero(50)

except Exception as e:
    print(f'Error: {e}')    

#Adicionalmente mostramos la información actual de cada usuario
print(bob.mostrar_info())
print(alicia.mostrar_info())