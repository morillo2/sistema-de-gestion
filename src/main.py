# Importa tus módulos aquí

from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Llama a mostrar_disponibles()
        mostrar_disponibles(libros)

    elif opcion == "2":
        # Llama a buscar_por_paginas()
        buscar_por_paginas(libros, 400)

    elif opcion == "3":
        # Llama contar_libros()
        # Llama promedio_paginas()
        
        print(f"Total de libros: {contar_libros(libros)}")
        print(f"Promedio de páginas: {promedio_paginas(libros):.2f}")


    elif opcion == "4":
        # ... completa las demás opciones

        print("Categorias actuales:", categorias)
        nueva = input("Escriba la nueva categoria: ")
        agregar_categoria(categorias, nueva)
        print("Categorias:", categorias)

    elif opcion == "5":
        print("Gracias por usar nuestro sistema de biblioteca.")
        break

    else:
        print("Opción no vigente. Intenta nuevamente.")
