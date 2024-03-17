import uuid

from Clases.Usuario import Usuario

class Cancion:
    def __init__(self, id: str, name: str, duration: str, link: str, reproducciones = 0, likes = []) -> None:
        if id == "":
            id = str(uuid.uuid5())
        self.id = id
        self.name = name 
        self.duration = duration
        self.link = link

        self.reproducciones = reproducciones

        self.likes = set(likes)

    # TODO - Usar API de Soundcloud
    def escuchar(self, usuario: Usuario):
        self.reproducciones += 1
        print(f"Escuchando canción {self.name} ({self.reproducciones} reproducciones totales)")
        usuario.escucharCancion(self.id)

    def like(self, usuarioLike: Usuario):
       if usuarioLike.id in self.likes:
            self.likes.remove(usuarioLike.id)
            usuarioLike.canciones_Like.remove(self.id)

            print(f"El usuario {usuarioLike.name}, le ha quitado un like a la canción {self.name}: {len(self.likes)} likes")
       else:
            self.likes.add(usuarioLike.id) 
            usuarioLike.canciones_Like.add(self.id) 

            print(f"El usuario {usuarioLike.name}, le ha dado un like a la canción {self.name}: {len(self.likes)} likes")

