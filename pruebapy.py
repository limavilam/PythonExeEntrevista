
#Contar vocales

entrada = ['a','o','u','w','f']

vocales = ['a','e','i','o','u']

def contar_vocales (entrada):
    contador = 0
    for i in entrada:
        if i in vocales:
            contador = contador + 1
    return contador

print(contar_vocales(entrada))


