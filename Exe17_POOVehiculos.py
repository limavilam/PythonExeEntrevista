class Vehiculo:
    
    #Método para iniciar los atributos

    """ Referencia a la instancia: Cuando se crea un objeto de una clase, se crea una nueva instancia de esa clase. 
    self se utiliza para referirse a esa instancia específica dentro de los métodos de la clase. """

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color=color
        self.encendido = False

    #Método para prender el carro
    def encender(self):
        if not self.encendido:
            self.encendido= True
            print(f"El vehiculo {self.marca} {self.modelo} está encendido")
        else:
            print(f"El vehiculo {self.marca} {self.modelo} ya está encendido")

    #Método para apagar el carro

    """self permite que la función apagar acceda y modifique los atributos del objeto específico que llama a esta función."""
    def apagar(self):
        if self.encendido:
            self.encendido=False
            print(f"El vehiculo {self.marca} {self.modelo} está apago")
        else:
            print(f"El vehiculo {self.marca} {self.modelo} ya estaba apago")
        
    #Método para mostrar la información del carro
    def info(self):
        if self.encendido:
            estado="encendido"
        else:
            estado="apagado"
        print(f"Vehiculo: {self.marca} {self.modelo}, color {self.color}, estado: {estado}")

#Crearemos un objetivo para la clase vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

#Usar los métodos
mi_vehiculo.info()
mi_vehiculo.encender()
mi_vehiculo.apagar()