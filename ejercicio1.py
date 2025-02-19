import re

def contar_palabras_unicas(texto: str) -> dict:
    
    texto = texto.lower()
    texto = re.sub(r'[^\w\sáéíóúüñ]', '', texto)
    palabras = texto.split()

    conteo = {}
    for palabra in palabras:
        if len(palabra) > 2:
            conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

texto = "¡Hola, hola! ¿Cómo estás? Espero que estés bien. Espero verte pronto."
resultado = contar_palabras_unicas(texto)
print(resultado)