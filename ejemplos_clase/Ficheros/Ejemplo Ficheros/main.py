import funciones as f
if __name__ == "__main__":
    paises = [
    {
        "nombre": "España",
        "poblacion": 49000000,
        "pib": 1700000,
        "capital": "Madrid",
        "idioma": "Español"
    },
    {
        "nombre": "Francia",
        "poblacion": 68000000,
        "pib": 3100000,
        "capital": "París",
        "idioma": "Francés"
    },
    {
        "nombre": "Alemania",
        "poblacion": 84000000,
        "pib": 4600000,
        "capital": "Berlín",
        "idioma": "Alemán"
    },
    {
        "nombre": "Italia",
        "poblacion": 59000000,
        "pib": 2300000,
        "capital": "Roma",
        "idioma": "Italiano"
    },
    {
        "nombre": "Portugal",
        "poblacion": 10600000,
        "pib": 300000,
        "capital": "Lisboa",
        "idioma": "Portugués"
    },
    {
        "nombre": "Brasil",
        "poblacion": 213000000,
        "pib": 2200000,
        "capital": "Brasilia",
        "idioma": "Portugués"
    },
    {
        "nombre": "Argentina",
        "poblacion": 46000000,
        "pib": 630000,
        "capital": "Buenos Aires",
        "idioma": "Español"
    },
    {
        "nombre": "México",
        "poblacion": 130000000,
        "pib": 1800000,
        "capital": "Ciudad de México",
        "idioma": "Español"
    },
    {
        "nombre": "Estados Unidos",
        "poblacion": 340000000,
        "pib": 29000000,
        "capital": "Washington D.C.",
        "idioma": "Inglés"
    },
    {
        "nombre": "Reino Unido",
        "poblacion": 69000000,
        "pib": 3500000,
        "capital": "Londres",
        "idioma": "Inglés"
    },
    {
        "nombre": "Japón",
        "poblacion": 124000000,
        "pib": 4100000,
        "capital": "Tokio",
        "idioma": "Japonés"
    },
    {
        "nombre": "China",
        "poblacion": 1410000000,
        "pib": 18700000,
        "capital": "Pekín",
        "idioma": "Mandarín"
    }
]
    
    f.escribir_informacion(paises)
    
    umbral_habitantes = 67000000
    
    

    
    lista_no_poblados = f.escribir_fichero_paises_poblados(umbral_habitantes)
    print("Los paises que no superan el umbral son: ", lista_no_poblados)