import csv


def generar_directorio():
    # lista para almacenar los directorios telefonicos
    directorio = []
    archivo_existe = False

    # Verificar si el archivo existe para determinar si agregar encabezados
    try:
        # Intentar abrir el archivo en modo lectura
        with open('directorio.csv', 'r') as archivo_csv:
            lector = csv.reader(archivo_csv)
            if any(lector):  # Comprobar si hay algún registro existente
                archivo_existe = True
    except FileNotFoundError:
        archivo_existe = False
    salida_bucle = "no";
    while salida_bucle == "no" or salida_bucle == "No":
        nombre = input("Ingrese su nombre: ")
        numero = input("Ingrese su numero telefonico: ")
        # agrega el registro al directorio
        directorio.append([nombre, numero])
        salida_bucle = input("desea continuar registrando? (si/no)")
    
    # Agregar nuevos registros al final o crear el archivo con encabezados
    with open('directorio.csv', 'a', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)

        if not archivo_existe:
            # Si el archivo no existe, agregar encabezados
            escritor.writerow(['nombre', 'numero'])

        # Escribir los nuevos registros al final del archivo
        for dir in directorio:
            escritor.writerow(dir)

    print("archivo guardado correctamente")



generar_directorio()
