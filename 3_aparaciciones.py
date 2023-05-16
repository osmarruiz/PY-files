def contar_palabra_en_fichero(palabra, nombre_fichero):
    try:
        with open(nombre_fichero, 'r') as archivo:
            contenido = archivo.read()
            apariciones = contenido.count(palabra)
            return apariciones
    except FileNotFoundError:
        return -1


# Solicitar la palabra y el nombre del fichero al usuario
palabra = input("Ingresa una palabra: ")
nombre_fichero = input("Ingresa el nombre del fichero: ")

# Contar las apariciones de la palabra en el fichero
cantidad_apariciones = contar_palabra_en_fichero(palabra, nombre_fichero)

# Verificar el resultado
if cantidad_apariciones == -1:
    print("El fichero no se encontró.")
else:
    if cantidad_apariciones == 1:
        print(f"La palabra '{palabra}' aparece {cantidad_apariciones} vez en el fichero.")
    else:
        print(f"La palabra '{palabra}' aparece {cantidad_apariciones} veces en el fichero.")