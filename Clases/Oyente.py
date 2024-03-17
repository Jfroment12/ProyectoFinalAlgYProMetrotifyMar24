from Clases.Usuario import Usuario


class Oyente(Usuario):
    def __init__(self, id: str, name: str, email: str, username: str) -> None:
        super().__init__(id, name, email, username, "listener")