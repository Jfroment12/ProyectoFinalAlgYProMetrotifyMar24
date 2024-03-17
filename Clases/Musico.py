from Clases.Album import Album
from Clases.Cancion import Cancion
from Clases.Usuario import Usuario


class Musico(Usuario):
    def __init__(self, id: str, name: str, email: str, username: str,
                  likes = []) -> None:
        super().__init__(id, name, email, username, "musician")

        self.likes = set(likes)


    def escogerCancion(self, albums: list[Album]):
        canciones_Del_Musico: list[Cancion] = []

        # Filtrar para conseguir solo las canciones del músico
        for album in albums:
            if album.artist == self.id:
                for cancion in album.tracklist:
                    canciones_Del_Musico.append(cancion)

        # Mostrar canciones
        index = 1
        for cancion in canciones_Del_Musico:
            print(f"{index}. {cancion.name}")
            index += 1

        # Seleccionar canciones
        while True:
            try:
                opcion = int(input("Escriba el número de la canción que desea")) - 1
                if opcion < 0:
                    print("Por favor no escriba valores negativos")
                    continue

                return canciones_Del_Musico[opcion]
            except:
                print("Ingrese un número por favor")

    def like(self, usuarioLike: Usuario):
       if usuarioLike.id in self.likes:
            self.likes.remove(usuarioLike.id)
            usuarioLike.musicos_Like.remove(self.id)

            print(f"El usuario {usuarioLike.name}, le ha quitado un like al músico {self.name}: {len(self.likes)} likes")
       else:
            self.likes.add(usuarioLike.id) 
            usuarioLike.musicos_Like.add(self.id) 

            print(f"El usuario {usuarioLike.name}, le ha dado un like al músico {self.name}: {len(self.likes)} likes")

