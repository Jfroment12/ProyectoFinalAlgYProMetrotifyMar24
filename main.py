import requests
from Clases.Album import Album
from Clases.Cancion import Cancion
from Clases.Musico import Musico
from Clases.Oyente import Oyente
from Clases.Playlist import Playlist
from Modulos.GestionIndicadores import GestionIndicadores
from Modulos.GestionIntereacciones import GestionInterraciones
from Modulos.GestionPerfil import GestionPerfil
from Modulos.GestionMusical import GestionMusical

#Proceso para tomar la data de Api

def main():
    oyentes, musicos = get_Users_API()
    albums = get_Albums_API()
    playlists = get_Playlists_API()

    menu(oyentes, musicos, albums, playlists)

def get_Users_API():
    request = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    
    users_JSON = request.json()

#Aqui comenzamos a crear y alimentar variables
        
    oyentes = []
    musicos = []
    for usuario in users_JSON:
        id = usuario["id"]
        name = usuario["name"].strip().title()
        username = usuario["username"]
        email = usuario["email"]
        type_Usuario = usuario["type"]

        if type_Usuario == "listener":
            oyente = Oyente(id, name, email, username)
            oyentes.append(oyente)
                 
        else:
            musico = Musico(id, name, email, username)
            musicos.append(musico)

    return oyentes, musicos      

def get_Albums_API():
    request = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")

    albums = request.json()

    albums_Objetos = []
    for album in albums:
        id = album["id"]
        name = album["name"]
        descripcion = album["description"]
        cover = album["cover"]
        published = album["published"]
        genre = album["genre"]
        artist = album["artist"]

        tracklist = album["tracklist"]
        canciones = []
        
        for track in tracklist:
            idCancion = track["id"]
            nameCancion = track["name"]
            duration = track["duration"]
            link = track["link"]

            cancion = Cancion(idCancion, nameCancion, duration, link)
            canciones.append(cancion)

        album_Objeto = Album(id, name, descripcion, cover, published, genre, artist, canciones)
        albums_Objetos.append(album_Objeto)

    return albums_Objetos

def get_Playlists_API():
    request = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")

    playlists = request.json()
    
    playlists_Objeto = []

    for playlist in playlists:
        id = playlist["id"]
        name = playlist["name"]
        descripcion = playlist["description"]
        creator = playlist["creator"]
        tracks = playlist["tracks"]

        playlist_Objeto = Playlist(id, name, descripcion, creator, tracks )
        playlists_Objeto.append(playlist_Objeto)

    return playlist_Objeto             
     
def menu(oyentes: list, musicos: list, albums: list, playlists: list):
    gestion_Perfil = GestionPerfil(oyentes, musicos, playlists, albums)
    gestion_Musical = GestionMusical(gestion_Perfil)
    gestion_Interacciones = GestionInterraciones(gestion_Perfil, gestion_Musical)
    gestion_Indicadores = GestionIndicadores(oyentes, musicos, playlists, albums)

    while True:
        try:
            opcion = int(input("""Seleccione la opcion de su preferencia                                
1. Gestión de perfil
2. Gestión de musical
3. Gestión de interacciones
4. Indicadores
5. Salir"""))

            if opcion == 1:
                gestion_Perfil.menu()
            elif opcion == 2:
                gestion_Musical.menu()
            elif opcion == 3:
                gestion_Interacciones.menu()
            elif opcion == 4:
                gestion_Indicadores.menu()
            elif opcion == 5:
                break
            else: 
                print("Escoja una de las opciones mostradas")

        except:
            print("Error! Ingrese un número válido")

main()