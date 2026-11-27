import funciones as f
if __name__ == "__main__":
    
    
    
    alumnos = {
    "Carlos García": ["Ingeniería Industrial", 8.5, 1001, 101, "1ºA"],
    "María López": ["Ingeniería Informática", 9.2, 1010, 102, "1ºB"],
    "Pablo Martínez": ["Ingeniería Industrial", 6.7, 1111, 201, "2ºA"],
    "Lucía Sánchez": ["Ingeniería Informática", 8.9, 1000, 202, "2ºB"],
    "Javier Fernández": ["Ingeniería Mecánica", 5.4, 1100, 301, "3ºA"],
    "Ana Rodríguez": ["Ingeniería Industrial", 9.5, 0000, 302, "3ºBC"],
    "Diego Pérez": ["Ingeniería Informática", 7.3, 1110, 101, "1A"]


}
    
    alumnos_mal = f.escribir_fichero(alumnos)
    
    
    # Podría crear el dicionario vacío aqui, mandarlo a la funcion (su direccion de memoria) 
    # y no devolverlo
    alumnos = f.leer_fichero()
    print(alumnos)
    
    
    