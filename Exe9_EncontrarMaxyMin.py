#Encontrar el máximo 

entrada = [15, 85, 35, 89, 125]

def encontrar_max(entrada):
    maximo = entrada[0]
    for i in entrada:
        if i > maximo:
            maximo = i
    return maximo

print("El número máximo es:",encontrar_max(entrada))


def encontrar_min(entrada):
    maximo = entrada[0]
    for i in entrada:
        if i < maximo:
            maximo = i
    return maximo

print(encontrar_min(entrada))

