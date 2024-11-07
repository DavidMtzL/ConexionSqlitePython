import funciones
while True:
    try:
      menu = int(input("[1] Para agregar una nueva pelicula [2] Pra obtener pelicula [3] Para salir del programa >>  "))

      if menu==1:
        funciones.agregar_pelicula()
      elif menu==2:
        funciones.obtener_peliculas()
      else:
        print("Saliendo del programa.....")
        exit()
    except ValueError as error:
        print(f"Ingrese el valor  valido  {error}")