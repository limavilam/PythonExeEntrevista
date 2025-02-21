# Hacer como un árbol de navidad
#        *
#       **
#      ***

pisos = 5

def construir_piramide(pisos):
    for i in range(pisos):
        espacios = pisos - i - 1
        asteriscos = 1 + i * 2
        print(" " * espacios + "*" * asteriscos)
    return

print(construir_piramide(pisos))



