
entrada = ['a','d','n','w','f']

vocales = ['a','e','i','o','u']

def contar_consonantes(entrada):
    contador = 0
    for i in entrada:
        if i  not in vocales:
            contador = contador + 1
    return contador

print(contar_consonantes(entrada))

