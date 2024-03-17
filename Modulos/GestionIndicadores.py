from Clases.Album import Album
from Clases.Musico import Musico
from Clases.Oyente import Oyente
from Clases.Playlist import Playlist
from Clases.Usuario import Usuario


class GestionIndicadores:
    def __init__(self, oyentes: list[Oyente], musicos: list[Musico], playlists: list[Playlist], albums: list[Album]) -> None:
        self.oyentes = oyentes
        self.musicos = musicos
        self.playlists = playlists
        self.albums = albums

    def menu(self):
        while True:
            try:
                opcion = int(input("""Bienvenido a la gestión de Indicadores                                
    1. Top 5 músicos con mayor cantidad de streams
    2. Top 5 álbumes con mayor cantidad de streams
    3. Top 5 canciones con mayor cantidad de streams
    4. Top 5 escuchas con mayor cantidad de streams
    5. Salir"""))

                if opcion == 1:
                    self.top5Musicos()
                elif opcion == 2:
                    self.top5Albums()
                elif opcion == 3:
                    self.top5Canciones()
                elif opcion == 4:
                    self.top5Escuchas()
                elif opcion == 5:
                    break
                else: 
                    print("Escoja una de las opciones mostradas")

            except:
                print("Error! Ingrese un número válido")

    
    
    def top5Musicos(self):
        musicos_Stream = {}
        for musicos in (self.musicos + self.oyentes):
            musicos_Stream[musicos.id] = [musicos.name, len(musicos_Stream)]

        self.top5(musicos_Stream)

    
    def top5Albums(self):
        albums_Stream = {}
        for album in self.albums:

            albums_Stream[album.id] = [album.name, 0]
            for cancion in album.tracklist:
                albums_Stream[album.id][1] += cancion.reproducciones

        self.top5(albums_Stream)

    def top5Canciones(self):
        # Clave (Id de la canción): Número de reproducciones
        canciones_Stream = {}
        for album in self.albums:
            for cancion in album.tracklist:
                canciones_Stream[cancion.id] = [cancion.name, cancion.reproducciones]

        self.top5(canciones_Stream)


    def top5Escuchas(self):
        usuarios_Stream = {}
        for usuario in (self.musicos + self.oyentes):
            usuarios_Stream[usuario.id] = [usuario.nombre, len(usuario.canciones_Escuchadas)]

        self.top5(usuarios_Stream)


    def top5(self, streams):
        # dict.items() -> [clave, valor] (1)
        # valor -> [nombre, reproducciones] (1)
        streams_Ordenados = sorted(streams.items(), reverse=True, key= lambda item: item[1][1])

        for position, objeto in enumerate(streams_Ordenados[:5]):
            nombre = objeto[1][0]
            reproducciones= objeto[1][0]

            print(f"Top {position +1}. {nombre}: {reproducciones}")            