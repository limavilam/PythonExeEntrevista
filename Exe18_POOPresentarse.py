class Persona:

    def __init__(self,nombre,edad,genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero

    def presentarse(self):
        print(f"Hola {self.nombre}, cuya edad es {self.edad} y género es {self.genero}")
    
    def es_mayor_de_edad(self):
        mayoria_edad=False
        if self.edad > 18:
            mayoria_edad=True
            print ("Es mayor de edad")
        else:
            mayoria_edad=False
            print ("Es menor de edad")

mi_persona = Persona("Mora",4,"Femenino")

mi_persona.presentarse()
mi_persona.es_mayor_de_edad()
