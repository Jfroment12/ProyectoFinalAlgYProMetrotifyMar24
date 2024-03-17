import uuid

from Clases.Usuario import Usuario
from Clases.Album import Album


class Playlist:
    def __init__(self, id: str, name: str, description: str, creator: str, tracks: list[str], likes = []) -> None:
        if id == "":
            id = str(uuid.uuid5())
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracks = tracks

        self.likes = set(likes)

    def escuchar(self, albums: list[Album], usuarioEscucha:Usuario):
        for album in albums:
            for cancion in album.tracklist:
                for cancionId in self.tracks:
                    if cancion.id == cancionId:
                        cancion.escuchar(usuarioEscucha)


    def like(self, usuarioLike: Usuario):
       if usuarioLike.id in self.likes:
            self.likes.remove(usuarioLike.id)
            usuarioLike.playlists_Like.remove(self.id)

            print(f"El usuario {usuarioLike.name}, le ha dado un like a la playlist {self.name}: {len(self.likes)} likes")
       else:
            self.likes.add(usuarioLike.id) #Guardo cuales usuarios le han dado like al álbum
            usuarioLike.playlists_Like.add(self.id) #Guardo a cuales albumes el usario ha dado like

            print(f"El usuario {usuarioLike.name}, le ha dado un like a la playlist {self.name}: {len(self.likes)} likes")