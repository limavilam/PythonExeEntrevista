class CuentaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, monto: float):
        self.saldo += monto

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