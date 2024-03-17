from Clases.Cancion import Cancion
import uuid

from Clases.Usuario import Usuario

class Album:
    def __init__(self, id: str, name: str, description: str, cover:str, published:str, 
                 genre: str, artist: str, tracklist: list[Cancion],
                 likes = []) -> None:
        if id == "":
            id = str(uuid.uuid5()) #Crear ID de un metodo que crea números/ids aleatoriamente
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist

        self.likes = set(likes)

    def escuchar(self, usuarioEscucha: Usuario):
        for cancion in self.tracklist:
            cancion.escuchar(usuarioEscucha)

    def like(self, usuarioLike: Usuario):
       if usuarioLike.id in self.likes:
            self.likes.remove(usuarioLike.id)
            usuarioLike.albums_Like.remove(self.id)

            print(f"El usuario {usuarioLike.name}, le ha dado un like al álbum {self.name}: {len(self.likes)} likes")
       else:
            self.likes.add(usuarioLike.id) #Guardo cuales usuarios le han dado like al álbum
            usuarioLike.albums_Like.add(self.id) #Guardo a cuales albumes el usario ha dado like

            print(f"El usuario {usuarioLike.name}, le ha dado un like al álbum {self.name}: {len(self.likes)} likes")


    