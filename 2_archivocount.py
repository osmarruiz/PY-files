

rutaArch = input("ingresa la ruta del archivo: ")

try:
    arch = open(rutaArch,'r')
    contador = 0;
    caracter = arch.read(1)
    contenido = arch.read()
    contador = len(contenido)
    arch.close();
    print("cantidad de caracteres del archivo: %d"%contador)
except IOError:
    print("ha ocurrido un error al abrir el archivo")
