def escribir_fichero(dic_alumnos:dict)-> list:
    
    f = open("alumnos.csv", "w", encoding = "UTF-8")
    nombres_alumnos_mal = []
    f.write("Nombre;carrera;notamedia;clave;aula;curso\n")
    for nombre, valor in dic_alumnos.items():        
        carrera = valor[0]
        nota_media = valor[1]
        clave_alumno = valor[2]
        aula = valor[3]
        curso = valor[4]
        # Una funcion que se encargue de limpiar el curso!!!
        
        # curso_limpio = limpiar_curso()
        
        if len(curso) == 3:
            linea = f"{nombre};{carrera};{nota_media};{clave_alumno};{aula};{curso}\n"
            f.write(linea)
        else:
            nombres_alumnos_mal.append(nombre)
            
            
    return nombres_alumnos_mal
        
           
    
    
    
    
    f.close()
    
    

def quitar_tildes(cadena):
    
    cadena_limpia = ""
    cadena = cadena.upper()
    
    dic_equivalencias = {"Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U"}
    
    
    for letra in cadena: 
        if letra in dic_equivalencias:
            cadena_limpia += dic_equivalencias[letra]
        else:
            cadena_limpia += letra

    # Ojo, consideramos que solo hay un nombre y un apellido
    # Si hubiese más nombres, más apellidos bla bla bla, deberías hacer un bucle. 
    
    # lista = cadena_limpia.split()
    # cadena_definitiva = ""
    # for elem in lista:
    #     cadena_definitiva += elem.capitalize() + " "
 
    nombre, apellido = cadena_limpia.split()
    cadena_definitiva = nombre.capitalize() + " " + apellido.capitalize()

    
    
    
    return cadena_definitiva
    
    
def obtener_numero_decimal(numero_binario:str):

    
    
    # contador = len(numero_binario)
    
    # while contador >= 0:
        
        
    #     contador -= 1
    suma = 0
    exponente = 0
    for pos in range(len(numero_binario)-1, -1, -1):
    
        suma += int(numero_binario[pos]) * (2 ** exponente)
        exponente += 1
        
    return suma
        
        
        
    
    
    
    
    
def leer_fichero()->dict:
    alumnos = {}
    f = open("alumnos.csv", "r", encoding = "UTF-8")
    header = f.readline()
    for linea in f:
        
        lista = linea.strip().split(";")
        
        nombre = lista[0]
        carrera = lista[1]
        nota_media = lista[2]
        clave = lista[3]
        aula = lista[4]
        curso = lista[5]
        
        nombre_limpio = quitar_tildes(nombre)
        carrera_limpia = quitar_tildes(carrera)
        clave_decimal = obtener_numero_decimal(clave)
        alumnos[nombre_limpio] = [carrera_limpia, nota_media, clave_decimal, aula, curso]
    
    
    f.close()
    return alumnos
    
    
    
    
    
    