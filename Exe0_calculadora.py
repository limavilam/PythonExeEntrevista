def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: División por cero"

def calculadora():
    print("Calculadora en Python")
    print("Operaciones disponibles: +, -, *, /")
    
    a = float(input("Ingrese el primer número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    b = float(input("Ingrese el segundo número: "))
    
    if operacion == '+':
        print("Resultado:", suma(a, b))
    elif operacion == '-':
        print("Resultado:", resta(a, b))
    elif operacion == '*':
        print("Resultado:", multiplicacion(a, b))
    elif operacion == '/':
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida")

calculadora()
