class Persona:
    def __init__(self, nombre):  # Constructor
        self.nombre = nombre

    def saludar(self):  # Método
        print(f"Hola, mi nombre es {self.nombre}")

p = Persona("Lina")
p.saludar()