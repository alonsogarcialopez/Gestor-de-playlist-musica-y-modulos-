def agregarCancion(playlist):
    print("\n--- Agregar Canción ---")
    titulo = input("Título de la canción: ").strip()
    while titulo == "":
        print("El título no puede quedar vacío.")
        titulo = input("Título de la canción: ").strip()

    artista = input("Artista: ").strip()
    while artista == "":
        print("El artista no puede quedar vacío.")
        artista = input("Artista: ").strip()

    cancion = {"titulo": titulo, "artista": artista}
    playlist += [cancion]
    print(f" '{titulo}' de {artista} agregada con éxito.")


def mostrarPlaylist(playlist):
    print("\n --- LISTA DE REPRODUCCIÓN --- ")

    contador = 0
    for c in playlist:
        contador += 1

    if contador == 0:
        print("La playlist está vacía.")
        return

    posicion = 1
    for c in playlist:
        print(f"{posicion}. {c['titulo']} - {c['artista']}")
        posicion += 1


def buscarCancion(playlist):
    print("\n--- Buscar Canción ---")

    contador = 0
    for c in playlist:
        contador += 1

    if contador == 0:
        print("La playlist está vacía.")
        return

    buscada = input("Ingresa el nombre de la canción a buscar: ").strip()
    encontrado = False
    cancionEncontrada = {}

    for c in playlist:
        if c["titulo"] == buscada:
            encontrado = True
            cancionEncontrada = c

    if encontrado == True:
        print(
            f" Canción encontrada: {cancionEncontrada['titulo']} - {cancionEncontrada['artista']}"
        )
    else:
        print(" La canción no fue encontrada en la playlist.")


def eliminarCancion(playlist):
    print("\n--- Eliminar Canción ---")

    contador = 0
    for c in playlist:
        contador += 1

    if contador == 0:
        print("La playlist está vacía.")
        return

    print("Canciones actuales en la playlist:")
    posicionMostrar = 1
    for c in playlist:
        print(f"{posicionMostrar}. {c['titulo']} - {c['artista']}")
        posicionMostrar += 1

    buscada = input(
        "Ingresa el título exacto de la canción que deseas eliminar: "
    ).strip()

    posicionAborrar = -1
    i = 0
    for c in playlist:
        if c["titulo"] == buscada:
            posicionAborrar = i
        i += 1

    if posicionAborrar != -1:
        del playlist[posicionAborrar]
        print(f" La canción '{buscada}' fue eliminada de la playlist.")
    else:
        print(" No se encontró ninguna canción con ese título.")


def guardarArchivo(playlist):
    print("\n--- Guardar Playlist en Archivo ---")

    contador = 0
    for c in playlist:
        contador += 1

    if contador == 0:
        print("La playlist está vacía. No hay nada que guardar.")
        return

    archivo = open("mi_playlist.txt", "w")
    archivo.write("=== MI LISTA DE REPRODUCCION ===\n")

    posicion = 1
    for c in playlist:
        archivo.write(f"{posicion}. {c['titulo']} - {c['artista']}\n")
        posicion += 1

    archivo.close()
    print("¡Archivo 'mi_playlist.txt' generado con éxito en tu carpeta!")