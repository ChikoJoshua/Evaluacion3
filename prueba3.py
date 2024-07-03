import os


archivo_libros = "biblioteca.libros"


def mostrar_menu():
    print("Bienvenido a la Biblioteca")
    print("Presione 1 para registrar un libro")
    print("Presione 2 para buscar libros por autor")
    print("Presione 3 para mostrar la lista de libros")
    print("Presione 4 para salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def registrar_el_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    genero = input("Ingrese el género del libro: ")
    with open(archivo_libros, "a") as archivo:
        archivo.write(f"{titulo},{autor},{genero}\n")
    print(f"El libro '{titulo}' se registró correctamente.")


def buscar_libro_por_autor():
    buscar_autor = input("Ingrese el nombre del autor: ")
    encontrados = []
    with open(archivo_libros, "r") as archivo:
        for linea in archivo:
            titulo, autor, genero = linea.strip().split(',')
            if autor.lower() == buscar_autor.lower():
                encontrados.append((titulo, autor, genero))
    if encontrados:
        print(f"Libros encontrados del autor '{buscar_autor}':")
        for libro in encontrados:
            print(f"Título: {libro[0]}, Autor: {libro[1]}, Género: {libro[2]}")
    else:
        print(f"No se encontraron libros del autor '{buscar_autor}'.")