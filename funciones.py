from modelo import Pelicula, Genero, Catalogo
import sql
def agregar_pelicula():
    nombre=str(input("Ingrese el noimbre de la pelicula que desea agregar: "))
    duracion= int(input("Ingrese la duracion en miinutos de la pelicula: "))
    genero= int(input("Ingrese el  genero de la pelicula: "))

    pelicula=Pelicula(nombre,duracion,genero) 
    sql.agregar_pelicula(pelicula)

catalogo = Catalogo("Pelicula de mafia")
def obtener_peliculas():
    peliculas= sql.obtener_peliculas()
    for pelicula in peliculas:
        guardar_pelicula=Pelicula(pelicula[1],pelicula[2],pelicula[3])
        catalogo.pelicula.append(guardar_pelicula)
    for pelicula in catalogo.pelicula:
        print(f"""\
               Nombre de la pelicula: {pelicula.nombre}
Duracion de la pelicula {pelicula.duracion} minutos
Genero de la pelicula {pelicula.genero}
              """)
