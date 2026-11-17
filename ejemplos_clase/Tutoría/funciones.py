def mostrar_alfabetos(alfabetos):
    
    
    for alfabeto, dic_alfabeto  in alfabetos.items():
        
        print(f"Vamos a mostrar las equivalencias de: {alfabeto}")
        
        for letra, equivalencia in dic_alfabeto.items():
            
            
            print(f"{letra} ->  {equivalencia}")
            
            
            
def cifrar(alfabetos, alfabeto, cadena):
    # cadena = "LUCAS"
    
    cadena_cifrada = ""
    
    
    for letra in cadena: 
        
        
        cadena_cifrada += alfabetos[alfabeto][letra] + " "
    return cadena_cifrada
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
   
        
    
    
    