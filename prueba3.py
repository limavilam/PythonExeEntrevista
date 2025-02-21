#Contar letras-ocurrencia de caracteres

entrada = "pepe grillo patikalvo"
caracter = "a"

letras = entrada.split()

def contar_repetidos(entrada):
    contador = 0
    for letra in entrada:
        if letra == caracter:
            contador = contador + 1
    return contador

print(contar_repetidos(entrada))

