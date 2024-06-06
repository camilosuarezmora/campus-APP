import json

print("========== CONOCE LOS CAMPERS Y TRAINERS POR CADA RUTA ==========")

try:
    ruta_ingresada = input("     Ingresa el nombre de la ruta que deseas consultar. \n>>")

    try:
        with open("datos//rutas.json", "r") as rutas:
            rutas_manejable = json.load(rutas)
    except FileNotFoundError:
        print("Error: El archivo 'rutas.json' no se encuentra.")
        rutas_manejable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'rutas.json'.")
        rutas_manejable = {}

    try:
        with open("datos//grupos.json", "r") as grupos:
            grupos_manejable = json.load(grupos)
    except FileNotFoundError:
        print("Error: El archivo 'grupos.json' no se encuentra.")
        grupos_manejable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'grupos.json'.")
        grupos_manejable = {}

    try:
        with open("datos//campers.json", "r") as campers:
            campers_manejable = json.load(campers)
    except FileNotFoundError:
        print("Error: El archivo 'campers.json' no se encuentra.")
        campers_manejable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'campers.json'.")
        campers_manejable = {}

    if ruta_ingresada in rutas_manejable:
        for trainer in rutas_manejable[ruta_ingresada]:
            for value in rutas_manejable[ruta_ingresada][trainer]:
                for llaves_campers in grupos_manejable:
                    print(llaves_campers)
    else:
        print(f"Error: La ruta '{ruta_ingresada}' no se encuentra en 'rutas.json'.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
