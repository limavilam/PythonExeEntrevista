#Palindromo

palabra = 'hola'

def palindromo(palabra):
    tamano_uso = int(len(palabra)/2)
    for i in range(tamano_uso):
        if palabra[i] != palabra[(len(palabra)-i-1)]:
            return False
    return True

print(palindromo(palabra))