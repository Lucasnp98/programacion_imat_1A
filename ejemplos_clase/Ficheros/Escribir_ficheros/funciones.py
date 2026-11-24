def eliminar_tildes(palabra):
    
    
    dic_equivalencias = {"Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U"}
    palabra_limpia = ""
    
    for letra in palabra:
        if letra.upper() in dic_equivalencias:
            palabra_limpia += dic_equivalencias[letra.upper()]
        else:
            palabra_limpia += letra
    

        
    
    
    
    
    return palabra_limpia.lower()