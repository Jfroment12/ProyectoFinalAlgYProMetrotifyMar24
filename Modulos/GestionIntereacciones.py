from Modulos.GestionPerfil import GestionPerfil
from Modulos.GestionMusical import GestionMusical

class GestionInterraciones:
    def __init__(self, gestionPerfil: GestionPerfil, gestionMusical: GestionMusical) -> None:
        self.gestionPerfil = gestionPerfil
        self.gestionMusical = gestionMusical

    def menu(self):
        while True:
            try:
                
                opcion = int(input("""Bienvenido a la gestión de Interacciones                                
1. Likear un músico
2. Likear un álbum
3. Likear una canción
4. Likear una playlist

4. Salir"""))

                if opcion == 1:
                    self.likeMusico()
                elif opcion == 2: #en esta opcion tambien hicimos la nro 4, que está relacionada con buscar
                    self.likeAlbum()
                elif opcion == 3:
                    self.likeCancion()
                elif opcion == 4:
                    self.likePlaylist()
                elif opcion == 5:
                    break
                else: 
                    print("Escoja una de las opciones mostradas")

            except:
                print("Error! I ngrese un número válido")

    def likeMusico(self):
        usuarioLike = self.gestionPerfil.buscarPerfiles()
        if usuarioLike == None:
            print("No existe ningún usuario con el nombre ingresado")
            return

        musico = self.gestionPerfil.buscarPerfiles(True)
        if musico == None:
            print("No existe ningún músico con el nombre ingresado")
            return

        musico.like(usuarioLike)


    def likeAlbum(self):
        usuarioLike = self.gestionPerfil.buscarPerfiles()
        if usuarioLike == None:
            print("No existe ningún usuario con el nombre ingresado")
            return

        album = self.gestionMusical.buscarAlbums()
        if album == None:
            print("No existe ningún álbum con el nombre ingresado")
            return

        album.like(usuarioLike)

   
    def likeCancion(self):
        usuarioLike = self.gestionPerfil.buscarPerfiles()
        if usuarioLike == None:
            print("No existe ningún usuario con el nombre ingresado")
            return

        cancion = self.gestionMusical.buscarCanciones()
        if cancion == None:
            print("No existe ninguna canción con el nombre ingresado")
            return

        cancion.like(usuarioLike)

    def likePlaylist(self):
        usuarioLike = self.gestionPerfil.buscarPerfiles()
        if usuarioLike == None:
            print("No existe ningún usuario con el nombre ingresado")
            return

        playlist = self.gestionMusical.buscarPlaylists()
        if playlist == None:
            print("No existe ninguna playlist con el nombre ingresado")
            return

        playlist.like(usuarioLike)