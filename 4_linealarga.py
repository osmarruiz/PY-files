def encontrar_linea_mas_larga(nombre_fichero):
    try:
        with open(nombre_fichero, 'r') as archivo:
            lineas = archivo.readlines()
            linea_mas_larga = max(lineas, key=len)
            return linea_mas_larga.strip()
    except FileNotFoundError:
        return None


# Solicitar el nombre del fichero al usuario
nombre_fichero = input("Ingresa el nombre del fichero: ")

# Encontrar la línea más larga en el fichero
linea_mas_larga = encontrar_linea_mas_larga(nombre_fichero)

# Verificar el resultado
if linea_mas_larga is None:
    print("El fichero no se encontró.")
else:
    print(f"La línea más larga del fichero es: {linea_mas_larga}")
