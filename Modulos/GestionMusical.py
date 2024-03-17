from Clases.Album import Album
from Clases.Cancion import Cancion
from Clases.Playlist import Playlist
from Clases.Usuario import Usuario
from Modulos.GestionPerfil import GestionPerfil
from datetime import datetime

class GestionMusical:
    def __init__(self, gestionPerfil: GestionPerfil) -> None:
        self.gestionPerfil = gestionPerfil

    def menu(self):
        while True:
            try:
                opcion = int(input("""Bienvenido a la gestión del Perfil                                
1. Crear un álbum musical
2. Escuchar música
3. Crear playlists
4. Salir"""))

                if opcion == 1:
                    self.crearAlbum()
                elif opcion == 2: #en esta opcion tambien se hizo la nro 4 del menu, que está relacionada con buscar
                    self.escucharMusica()
                elif opcion == 3:
                    self.crearPlaylist()
                elif opcion == 4:
                    break
                else: 
                    print("Escoja una de las opciones mostradas")

            except:
                print("Error! Ingrese un número válido")

    def crearAlbum(self):
        name = input("Escriba el nombre de su nuevo álbum").strip().title()
        description = input("Escriba la descripción de su nuevo álbum")
        cover = input("Ingrese el link del cover de su nuevo álbum")
        published = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ') #Libreria para registrar formato de fecha
        genre = input("Ingrese el género de su nuevo álbum: ")

        artist = None
        while artist == None:
            artist = self.gestionPerfil.buscarPerfiles(True)
            if artist == None:
                print("No existe un músico con ese nombre")
                continue
            break
        
        tracklist = []
        while True:
            cancion = self.crearCancion()
            tracklist.append(cancion)

            while True: #Validar que solo si o no
                seguirCreando = input("Desea crear otra canción? (Si/No)").strip().title()

                if seguirCreando != "Si" and seguirCreando != "No":
                    print("Ingrese solo Si o No") #Se insite en este tipo de validaciones ya que usuario a veces coloca cualquier respuesta incohernte
                    continue
                break

            if seguirCreando == "Si":
                continue
            elif seguirCreando == "No":
                break

        album = Album("", name, description, cover, published, 
                genre, artist.id, tracklist)
        self.gestionPerfil.albums.append(album)
        
    def crearCancion(self):
        name = input("Escriba el nombre de su nueva canción").strip().title()
        duration = self.escribirDuracion()
        link = input("Escriba el link de la música de su nueva canción")

        cancion = Cancion("", name, duration, link)
        return cancion

    def escribirDuracion(self):
        while True:
            try:
                minutos = int(input("Ingrese la duración en minutos de su canción: "))

                if minutos < 0 or minutos >= 60:
                    print("Ingrese un valor entre 0 y 59")
                    continue
                break

            except:
                print("Por favor ingresa un número")
        
        while True:
            try:
                segundos = int(input("Ingrese la duración en segundos de su canción: "))

                if segundos < 0 or segundos >= 60:
                    print("Ingrese un valor entre 0 y 59")
                    continue
                break

            except:
                print("Por favor ingresa un número")

        strMinutos = str(minutos)
        if len(strMinutos) == 1:
            strMinutos = "0" + strMinutos

        strSegundos = str(segundos)
        if len(strSegundos) == 1:
            strSegundos = "0" + strSegundos

        duracionString = f"{strMinutos}: {strSegundos}"
        return duracionString

    def escucharMusica(self):
        while True:
            try:
                print("Ingrese el nombre del usuario que va a escucahr una canción:")
                usuarioEscucha = self.gestionPerfil.buscarPerfiles()
                if usuarioEscucha == None:
                    print("No existe ningún usuario con ese nombre")

                opcion = int(input("""Escoja por cuál método quiere escuchar una canción                     
1. Buscar por álbum 
2. Buscar por canción
3. Buscar por perfil del músico
4. Buscar por una playlist
5. Salir"""))

                if opcion == 1:
                    self.escucharPorAlbum(usuarioEscucha)
                elif opcion ==2:
                    self.escucharPorCancion(usuarioEscucha)
                elif opcion == 3:
                    self.escucharPorMusico(usuarioEscucha)
                elif opcion == 4:
                    self.escucharPorPlaylist(usuarioEscucha)
                elif opcion == 5:
                    break
                else: 
                    print("Escoja una de las opciones mostradas")

            except:
                print("Error! Ingrese un número válido")

    def escucharPorAlbum(self, usuarioEscucha: Usuario):
        album = self.buscarAlbums()
        if album == None:
            print("No existe ningún álbum con el nombre ingresado")
            return
        album.escuchar(usuarioEscucha)

    def escucharPorCancion(self, usuarioEscucha: Usuario):
        cancion = self.buscarCanciones()
        if cancion == None:
            print("No existe ninguna canción con el nombre ingresado")
            return

        cancion.escuchar(usuarioEscucha)
    
    def escucharPorMusico(self, usuarioEscucha: Usuario):      
        musico = self.gestionPerfil.buscarPerfiles(True)
        if musico == None:
            print("No existe músico con dicho nombre")
            return

        albums = self.gestionPerfil.albums
        cancion = musico.escogerCancion(albums)
        cancion.escuchar(usuarioEscucha)
    
    def escucharPorPlaylist(self, usuarioEscucha: Usuario):
        playlist = self.gestionPerfil.buscarPerfiles(True)
        if playlist == None:
            print("No existe playlist con dicho nombre")
            return

        albums = self.gestionPerfil.albums
        playlist.escuchar(albums, usuarioEscucha)

    def buscarAlbums(self):
        nombre = input("Ingrese el nombre del álbum que desea buscar")
        for album in self.gestionPerfil.albums:
            if album.name == nombre:
                return album

    def buscarCanciones(self):
        nombre = input("Ingrese el nombre de la canción que desea buscar")
        for album in self.gestionPerfil.albums:
            for cancion in album.tracklist:
                if cancion.name == nombre:
                    return cancion

    def buscarPlaylists(self):
        nombre = input("Ingrese el nombre de la playlist que desea buscar")

        for playlist in self.gestionPerfil.playlists:
            if nombre == playlist.name:
                return playlist
        
    def crearPlaylist(self):
        name = input("Escriba el nombre de su nueva playlist").strip().title()
        description = input("Escriba la descripción de su nueva playlist")

        creator = self.gestionPerfil.buscarPerfiles()
        if creator == None:
            print("No existe ningún usuario con ese nombre")
            return
        
        tracks = []
        while True:	
            cancion = self.buscarCanciones()
            if cancion == None:
                print("No existe ninguna canción con ese nombre")
                continue
            tracks.append(cancion.id)

            while True: #Validar que solo si o no
                seguirCreando = input("Desea crear otra canción? (Si/No)").strip().title()

                if seguirCreando != "Si" and seguirCreando != "No":
                    print("Ingrese solo Si o No")
                    continue
                break

            if seguirCreando == "Si":
                continue
            elif seguirCreando == "No":
                break

        playlist = Playlist("", name, description, creator.id, tracks)
        listaPlaylist = self.gestionPerfil.playlists

        listaPlaylist.append(playlist)

