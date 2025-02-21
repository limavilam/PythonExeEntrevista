class CuentaBancaria:

    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0.0  #No se pasa como argumento
    
    def depositar(self,monto):
        self.saldo = self.saldo + monto
        print("El saldo actual es", self.saldo)
        

    def retirar(self, monto: float):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Error: Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta = CuentaBancaria("Carlos")
cuenta.depositar(100)
cuenta.retirar(30)
cuenta.mostrar_saldo()
    