import funciones as f
alfabetos = {
    "morse": {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."
    },

    "radiofonico": {
        "A": "Alfa",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }
}




# f.mostrar_alfabetos(alfabetos)

cadena = input("Introduce una cadena: ").upper()

alfabeto = "radiofonico"
cifrado = f.cifrar(alfabetos, alfabeto, cadena)


print(f"La cadena {cadena} cifrada en {alfabeto} es {cifrado}")








lista = ["Ana", "Dani", "Jose"]

# lista.append("Jose")
# lista.index("Ana") -> devuelve la posicion de algo en una lista




for clave in alfabetos:
    print(clave) #Recorro las claves del diccionario
    print(alfabetos[clave]) #A partir de la clave saco el valor
    
    

for clave in alfabetos.keys():
    print(clave) #Recorro las claves del diccionario
    print(alfabetos[clave]) #A partir de la clave saco el valor
    

    
    
for valor in alfabetos.values():
    print(valor) #recorre el valor directamente (un dic en este caso)

for clave, valor in alfabetos.items():
    print(clave, valor) #Recorre claves y valores a la vez












