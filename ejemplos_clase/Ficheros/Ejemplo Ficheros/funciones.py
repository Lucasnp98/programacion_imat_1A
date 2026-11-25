def escribir_informacion(paises:list)-> None:
    
    f = open("paises.csv", "w", encoding = "UTF-8")
    
    header = "pais,poblacion,pib,capital,idioma\n"
    f.write(header)
    
    for dic_pais in paises:
        nombre = dic_pais["nombre"]
        poblacion = dic_pais["poblacion"]
        pib = dic_pais["pib"]
        capital = dic_pais["capital"]
        idioma = dic_pais["idioma"]
        
        #f.write(poblacion) ESTO NO FUNCIONA XQ EN LOS FTEXTO, ESCRIBIMOS STRINGS
        #CUANDO YO HAGO UN FSTRING, CONVIERTO TODO A STRING
        linea = f"{nombre},{poblacion},{pib},{capital},{idioma}\n"
        f.write(linea)
    
    
    f.close()
    
    
def escribir_fichero_paises_poblados(umbral:int) -> list:
    """ 
    Mi idea es que mi funcion reciba un umbral de habitantes y,
    leyendo el fichero de paises.csv, cree otro fichero llamado paises
    poblados.csv sólo con aquellos paises que superen ese umbral de habitantes. 
    El formato de este fichero simplemente es pais:poblacion. El resto de campos los ignoro
    Además, deberá devolver al programa principal una lista con los nombres de los paises 
    que no han superado ese umbral
    """
    
    
    f_paises = open("paises.csv", "r", encoding = "UTF-8")

    f_paises_poblados = open("paises_poblados.txt", "w", encoding = "UTF-8")
    
    header = f_paises.readline()
    
    lista_paises_no_poblados = []
    
    for linea in  f_paises:
        
        lista = linea.strip().split(",")
        nombre = lista[0]
        poblacion = int(lista[1])
        
        if poblacion > umbral: 
            linea = f"{nombre}:{poblacion}\n"
            f_paises_poblados.write(linea)
        else:
            lista_paises_no_poblados.append(nombre)
            
    f_paises_poblados.close()
        
    f_paises.close()
    
    
    return lista_paises_no_poblados
    
    