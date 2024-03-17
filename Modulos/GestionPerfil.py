from Clases.Album import Album
from Clases.Musico import Musico
from Clases.Oyente import Oyente
from Clases.Playlist import Playlist



class GestionPerfil:
    def __init__(self, oyentes: list[Oyente], musicos: list[Musico], playlists: list[Playlist], albums: list[Album]) -> None:
        self.oyentes = oyentes
        self.musicos = musicos
        self.playlists = playlists
        self.albums = albums

    def menu(self):
        while True:
            try:
                opcion = int(input("""Bienvenido a la gestión del Perfil                                
    1. Registar nuevos usuarios
    2. Buscar perfiles
    3. Cambiar información personal
    4. Borrar los datos de la cuenta
    5. Salir"""))

                if opcion == 1:
                    self.registrar()
                elif opcion == 2:
                    self.accederCuenta()
                elif opcion == 3:
                    self.cambiarInformacion()
                elif opcion == 4:
                    self.borrarUsuario()
                elif opcion == 5:
                    break
                else: 
                    print("Escoja una de las opciones mostradas")

            except:
                print("Error! Ingrese un número válido")

    def registrar(self):
        name = input("Ingrese su nombre: ").strip().title() #se coloca strip para quitar espacios y title para poner may 1era letra
        e_mail = input("Ingrese su e_mail: ").strip()
        username = input("Ingrese su nombre de usuario: ").strip()

        while True:
            tipo_Usuario = input("Usted es oyente o musico?: ").strip().lower() #aqui definimos si es oyente o musico


            if tipo_Usuario != "oyente" and tipo_Usuario != "musico":
                continue
            break
        if tipo_Usuario == "oyente":
            oyente = Oyente("", name, e_mail, username)
            self.oyentes.append(oyente)

        elif tipo_Usuario == "musico":
            musico = Musico("", name, e_mail, username)
            self.musicos.append(musico)

    def buscarPerfiles(self, soloMusicos = False):
        nombre = input("Ingrese el nombre del usuario que desea buscar").strip().title()

        if soloMusicos == True:
            usuarios = self.musicos
        else:
            usuarios = self.oyentes + self.musicos

        for usuario in usuarios:
            if usuario.name == nombre:
                return usuario

    def cambiarInformacion(self):
        usuario = self.buscarPerfiles()

        while True:
            try:
                opcion = int(input("""Seleccione que campo desea modificar                      
    1. Nombre
    2. Email
    3. Username
    4. Salir"""))

                if opcion == 1:
                    nombre = input("Escriba su nuevo nombre: ")

                    print(f"Se ha cambiado el nombre exitosamente! ({usuario.nombre} -> {nombre})")
                    usuario.nombre = nombre
                elif opcion == 2:
                    email = input("Escriba su nuevo email: ")

                    print(f"Se ha cambiado el email exitosamente! ({usuario.email} -> {email})")
                    usuario.email = email
                elif opcion == 3:
                    username = input("Escriba su nuevo username:  ")

                    print(f"Su username ha sido cambiado exitosamente! ({usuario.username} -> {username})")
                    usuario.username = username             
                elif opcion == 4:
                    break
                else: 
                    print("Escoja una de las opciones mostradas")

            except:
                print("Error! Ingrese un número válido")

    def borrarUsuario(self):
        usuario = self.buscarPerfiles()
        if usuario == None:
            print("No existe ningun usuario con ese nombre")
            return 
        
        for index, oyente in enumerate(self.oyentes): #Método de Borrado de un elemento de usuario,  bien sea Oyente o Músico
            if usuario.id == oyente.id:
                self.oyentes.pop(index)

        for index, musico in enumerate(self.musicos):
            if usuario.id == musico.id:
                self.musicos.pop(index)

    def accederCuenta(self):
        usuario = self.buscarPerfiles()

        # TODO terminar
        print(usuario)