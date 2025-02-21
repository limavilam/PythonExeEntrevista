
entrada = "pepe grillo patikalvo"
#caracter = "a"

letras = entrada.split()

def contar_repetidos(entrada,caracter):
    contador = 0
    for letra in entrada:
        if letra == caracter:
            contador = contador + 1
    return contador

#print(contar_repetidos(entrada))

vocales = ['a','e','i','o','u']

for vocal in vocales:
    print(f'La vocal {vocal} esta:{contar_repetidos(entrada,vocal)} veces')
