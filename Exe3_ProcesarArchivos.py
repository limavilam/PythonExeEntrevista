def procesar_archivo(nombre_archivo: str):
    
    try:
        with open(nombre_archivo, 'r') as archivo:

            suma = 0
            contador = 0

            for linea in archivo:
                linea = linea.strip()
                if linea:
                    try:
                        numero = int(linea)
                        suma += numero
                        contador += 1
                    except ValueError:
                        print(f"Error: Línea no válida '{linea}' en el archivo.")

            if contador > 0:
                promedio = suma / contador
                with open('resultado.txt', 'w') as archivo_resultado:
                    archivo_resultado.write(f"Suma: {suma}\n")
                    archivo_resultado.write(f"Promedio: {promedio}\n")
                print("Suma y promedio calculados y guardados en resultado.txt")
            else:
                print("No se encontraron números válidos en el archivo.")

    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")

procesar_archivo('datos.txt')