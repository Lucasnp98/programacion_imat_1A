def crear_diccionario(num:int) -> dict:
    
    jugadores = {}
    
    for i in range(num):
       
        nombre = pedir_validar_clave(jugadores)
        goles = int(input("Introduce los goles: "))
        pat = input("Introduce el pat: ")
        equipo = input("Introduce el equipo: ")
        
        jugadores[nombre] = {"goles":goles, "patrocinador":pat, "equipo":equipo}
        
    return jugadores


def pedir_validar_clave(jugadores:dict) -> str:
    nombre = input("Nombre: ")
    while nombre in jugadores.keys():
        print("Ya tenemos ese jugador, prueba de nuevo")
        nombre = input("Nombre: ")
    return nombre
    
    
def maximo_goleador(jugadores:dict) -> tuple:
    
    
    maximo = 0
    for nombre, dic_jugador in jugadores.items():
        
        goles_jugador = dic_jugador["goles"]
        if goles_jugador > maximo:
            maximo = goles_jugador
            goleador_maximo  = nombre  
        
    return goleador_maximo, maximo
    
        
    
    
    
    
    
    
    return goleador_maximo, goles
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
        
        
        
    