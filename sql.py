import sqlite3
from constantes import *
from modelo import Pelicula

def conectar_db():
    conexion= sqlite3.connect(DATABASE_NAME)
    cursor= conexion.cursor()
    return conexion, cursor

def agregar_pelicula(pelicula):
    conexion,cursor=conectar_db()
    pelicula=(
           pelicula.nombre,
           pelicula.duracion,
           pelicula.genero
    )
    sql=f"INSERT INTO pelicula (nombre,duracion,genero) VALUES {pelicula};"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def obtener_peliculas():
    conexion,cursor=conectar_db()
    sql="select * from pelicula;"
    cursor.execute(sql)
    peliculas= cursor.fetchall()
    cursor.close()
    return peliculas


