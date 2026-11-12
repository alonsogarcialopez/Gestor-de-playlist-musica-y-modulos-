from menu import mostrarMenu
from operaciones import (
    agregarCancion,
    mostrarPlaylist,
    buscarCancion,
    eliminarCancion,
    guardarArchivo,
)

playlist = []
opcion = ""

while opcion != "6":
    mostrarMenu()
    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
        registrar = agregarCancion(playlist) 
    elif opcion == "2":
        mostrarPlaylist(playlist)
    elif opcion == "3":
        buscarCancion(playlist)
    elif opcion == "4":
        eliminarCancion(playlist)
    elif opcion == "5":
        guardarArchivo(playlist)
    elif opcion == "6":
        print("Saliendo de la playlist. byeee")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")