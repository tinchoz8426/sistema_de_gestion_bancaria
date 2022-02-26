import time # Importamos el modulo time para simular tiempos de carga con time.sleep()

# Clase padre
class Usuario():
    def __init__(self, nombre, edad, genero, numero_de_cuenta):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.numero_de_cuenta = numero_de_cuenta

    def mostrar_detalles(self):
        print(f"Información personal\nNombre: {self.nombre}\nEdad: {self.edad}\ngenero: {self.genero}")


# Clase hija
class Banco(Usuario):
    def __init__(self, nombre, edad, genero, numero_de_cuenta):
        super().__init__(nombre, edad, genero, numero_de_cuenta)
        self.balance = 0
    
    def depositar(self, cantidad):
        self.cantidad = cantidad
        self.balance = self.balance + self.cantidad
        print(f"Depositando {self.cantidad} ARS. El balance se esta actualizando...")
        time.sleep(5)
        print(f"El balance de la cuenta se ha actualizado: {self.balance} ARS\n")
    
    def retirar(self, cantidad):
        self.cantidad = cantidad
        print("Consultando si dispone de saldo...")
        time.sleep(5)
        if self.cantidad > self.balance :
            print(f"Fondos insuficientes | Balance: {self.balance}\n")
        else:
            self.balance = self.balance - self.cantidad
            print("Retirando dinero...")
            time.sleep(5)
            print(f"Has retirado {self.cantidad}\nEl balance de la cuenta se ha actualizado: {self.balance} ARS\n")

    def mostrar_balance(self):
            print("Accediendo a sus datos...")
            time.sleep(5)
            self.mostrar_detalles()
            print(f"Su saldo es de : {self.balance} ARS\n")

carlos = Banco("Carlos", 54, "Masculino", 616756)


print(f"Bienvenido a nuestro sistema bancario {carlos.nombre}\nEstamos accediendo a su cuenta...\n")
time.sleep(3)
# Bucle para el menu de opciones
while True:

    seleccion=int(input("Selecciona una opción:\n1-Mostrar datos de su cuenta\n2-Realizar un deposito\n3-Realizar un retiro\n4-Para salir del sistema\n-->"))

    if seleccion == 1:
        carlos.mostrar_balance()
    elif seleccion == 2:
        carlos.depositar(int(input("¿Cuanto dinero desea depositar?")))
    elif seleccion == 3:
        carlos.retirar(int(input("¿Cuanto dinero desea retirar?")))
    else:
        print("Gracias por utilizar nuestro sistema bancario")
        break
