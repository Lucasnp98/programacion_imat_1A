def leer_fichero_autores(autores:dict)-> dict:
    f = open("libros.txt", "r", encoding = "UTF-8")
    
   
    
    
    header = f.readline()
    for linea in f:
        linea_sin_barran = linea.strip()
        lista = linea_sin_barran.split(";")
        autor = lista[0]
        titulo = lista[1]
        puntuacion = float(lista[2])
        edad = lista[3]
        isbn = lista[4]
        editorial = lista[5]
        if puntuacion < 0:
            print("Hemos detectato una valoracion incorrecta", linea)
        if autor != "Sin autor" and puntuacion > 0:
            autores[autor] = [titulo, puntuacion, edad, isbn, editorial]
    
    f.close()
    
    
    
# def leer_fichero_autores()-> dict:
#     f = open("libros.txt", "r", encoding = "UTF-8")
    # autores = {}
   
    
    
#     header = f.readline()
#     for linea in f:
#         linea_sin_barran = linea.strip()
#         lista = linea_sin_barran.split(";")
#         autor = lista[0]
#         titulo = lista[1]
#         puntuacion = float(lista[2])
#         edad = lista[3]
#         isbn = lista[4]
#         editorial = lista[5]
#         autores[autor] = [titulo, puntuacion, edad, isbn, editorial]
    
#     f.close()
# return autores
    
    
    
    
def obtener_libros_autor(autor:str)-> list:
    f = open("libros.txt", "r", encoding = "UTF-8")
    libros_autor = []
    header = f.readline()
    for linea in f:
        linea_sin_barran = linea.strip()
        lista = linea_sin_barran.split(";")
        autor_fichero = lista[0]
        libro = lista[1]
        
        
        if autor_fichero == autor:
            libros_autor.append(libro)
            
    
    
    
    f.close()
    return libros_autor

    