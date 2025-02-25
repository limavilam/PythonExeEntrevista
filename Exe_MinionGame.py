
palabra = 'banana'
#palabra ='cuaderno'
#palabra = 'patikalvo'
vocales = 'aeiou'

def minion_game(palabra):
    vocal = 0
    consonante = 0
    tamano_palabra = len(palabra)

    #Kevin
    for i in range(tamano_palabra):
        print("El valor de i: ",i)
        if palabra[i] in vocales:
            print ("Palabra es:" , palabra[i:])
            print("Tamaño palabra:" , tamano_palabra)
            vocal = vocal + tamano_palabra - i
            print("Los puntos vocales:", vocal)
            print(palabra[i])
        else:
            consonante = consonante + tamano_palabra - i
            print("Puntos consonante:" , consonante)

minion_game(palabra)

#for i in range(0,len(palabra)+1):
#    print(palabra[:i])
            



#if __name__ == '__main__':