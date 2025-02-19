def filtrar_productos(productos: dict, precio_min: float) -> list:

    productos_filtrados =[]

    for producto, precio in productos.items():
        if precio >= precio_min:
            productos_filtrados.append(producto)
    return productos_filtrados

productos = {
    "manzana": 1.2,
    "banana": 0.8,
    "pera": 1.5,
    "uva": 2.0
}

resultado = filtrar_productos(productos, 1.0)
print(resultado)