import funciones as f

if __name__ == "__main__":
    
    numero_jugadores = 3
    #jugadores = f.crear_diccionario(numero_jugadores)
    jugadores = {'Mbappe': {'goles': 50, 'patrocinador': 'Nike', 'equipo': 'RM'}, 'Zidane': {'goles': 70, 'patrocinador': 'Adidas', 'equipo': 'RM'}, 'Lamine': {'goles': 13, 'patrocinador': 'Adidas', 'equipo': 'Barsa'}, 'Vinicius': {'goles': 3, 'patrocinador': 'Nike', 'equipo': 'RM'}, 'Arda guller': {'goles': 12, 'patrocinador': 'Nike', 'equipo': 'RM'}}
    
    print(jugadores)
    
    nombre_maximo, goles_maximos = f.maximo_goleador(jugadores)
    
    print(f"El maximo goleador es: {nombre_maximo} y ha metido {goles_maximos}")
    