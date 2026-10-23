from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros"""
    if len(libros) == 0:
        return 0
    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)

def contar_libros(libros: list[Libro]):
    """Retorna la cantidad total de libros"""
    return len(libros)

# Funciones que debes implementar
def mostrar_disponibles(lista_libros: list[Libro]):
    """Muestra solo los libros que están disponibles"""
    # Implementan la lógica aquí
    
    buscar = False

    for libro in lista_libros:

       if libro["disponible"]:
            print(
                f"Titulo: {libro["titulo"]}   -"
                f"Autor: {libro["autor"]}     -"
                f"Paginas: {libro["paginas"]}  "
                )
            buscar = True
    
    if not buscar:
        print("Por el momento no hay libros disponibles")
        

def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    """Muestra libros con menos páginas que max_paginas"""
    # Implementan la lógica aquí

    buscar = False

    for libro in lista_libros:

       if libro["paginas"] < max_paginas:

        print(
            f"Titulo: {libro["titulo"]}   -"
            f"Autor: {libro["autor"]}     -"
            f"Paginas: {libro["paginas"]}  "
            )
        buscar = True

   
def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    """Agrega una nueva categoría al set"""
    # Implementan la lógica aquí
    
    nueva_categoria = nueva_categoria.strip()

    if not nueva_categoria:
        print("La categoria no debe de estar vacia")
        return

    if nueva_categoria in set_categorias:
        print("La categoria ya existe")
    else:
        print(f"Categoria '{nueva_categoria}' agregada")
