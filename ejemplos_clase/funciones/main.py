
import funciones as f


if __name__ == "__main__":
    n1 = 2
    n2 = 3
    n3 = 6
    
    
    op = 0
    while op != 5: 
        
        op = int(input("Introduce una op: "))
        while op < 1 or op > 5: 
            print("Error")
            op = int(input("Introduce una op: "))
            
            
            
        if op == 1: 
            resultado = f.suma(n1, n2)
        elif op == 2:
            resultado = f.resta(n1, n3)
        elif op == 3: 
            resultado = f.multiplicacion(n3, 4)
        elif op == 4: 
            resultado = f.division(49, 7)
            
        f.mostrar_resultado(resultado)
            
        

    
    