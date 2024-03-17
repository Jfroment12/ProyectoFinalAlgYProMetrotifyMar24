import uuid


class Usuario:
    def __init__(self, id: str, name: str, email:str, username: str, tipo: str, 
                 canciones_Escuchadas = [], albums_Like = [], musicos_Like = [], canciones_Like = [], playlists_Like = []) -> None:
        if id == "":
            id = str(uuid.uuid5())
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.tipo = tipo

        # Se usa el copy para asegurarme de que cada usuario tenga su propia lista
        self.canciones_Escuchadas = canciones_Escuchadas.copy()

        self.albums_Like = set(albums_Like)
        self.musicos_Like = set(musicos_Like)
        self.canciones_Like = set(canciones_Like)
        self.playlists_Like = set(playlists_Like)

    def escucharCancion(self,  cancionId):
        self.canciones_Escuchadas.append(cancionId)
