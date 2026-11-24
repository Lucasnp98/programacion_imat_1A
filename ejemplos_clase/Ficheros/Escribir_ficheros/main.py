import funciones as f

# f = open("fichero.txt", "w", encoding = "UTF-8")

# nombres = ["Lucas","Ana", "Dani", "Sofía", "Judith"]
# notas = [4,5,4,5,8]
# carreras = ["GITT", "ENF", "ENERGÍA", "IMAT", "IMAT"]


# for pos in range(len(nombres)):
    
#     linea = f"{nombres[pos]}:{notas[pos]}:{carreras[pos]}\n"
#     f.write(linea)
    
# f.close()





# tiendas = {"Zara":[60, 80, 90], "PULL":[50,40,30], "Nike":[40,50,30]}
# Volcar la información de mi diccionario en un fichero llamado tiendas.txt.
# El formato es: tienda;venta1;venta2;venta3

# f = open("ventas.txt", "w", encoding = "UTF-8")

# header = "tienda;venta1;venta2;venta3\n"
# f.write(header)
# for tienda in tiendas: 
#     venta1 = tiendas[tienda][0]
#     venta2 = tiendas[tienda][1]
#     venta3 = tiendas[tienda][2]
    
    
#     linea = f"{tienda};{venta1};{venta2};{venta3}\n"

#     f.write(linea)

# f.close()




alumnos = {"Sofía":["GITT", 7, 29], "María":["FISICA", 8, 28]}


fichero = open("alumnos.csv", "w", encoding = "UTF-8")
header = "nombre_sin_tilde;carrera;nota;edad\n"
fichero.write(header)

for nombre in alumnos:
    nombre_sin_tilde = f.eliminar_tildes(nombre)

    carrera = alumnos[nombre][0]
    nota = alumnos[nombre][1]
    edad = alumnos[nombre][2]
    linea = f"{nombre_sin_tilde};{carrera};{nota};{edad}\n"
    fichero.write(linea)




fichero.close()








