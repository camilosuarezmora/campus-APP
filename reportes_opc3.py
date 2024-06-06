import json

try:
    with open("datos//trainers.json", "r") as trainers:
        try:
            dicc_trainers = json.load(trainers)
        except json.JSONDecodeError:
            print("Error: No se pudo decodificar el archivo 'trainers.json'.")
            dicc_trainers = {}
except FileNotFoundError:
    print("Error: El archivo 'trainers.json' no se encuentra.")
    dicc_trainers = {}
except Exception as e:
    print(f"Ocurrió un error inesperado al abrir 'trainers.json': {e}")
    dicc_trainers = {}

if dicc_trainers:
    print("========== CONOCE LOS TRAINERS ==========")
    print("Los trainers que se encuentran trabajando con campuslands son: ")
    for profesores in dicc_trainers.keys():
        print(f"    *{profesores}")
else:
    print("No se encontraron datos en 'trainers.json' o el archivo no se pudo cargar correctamente.")
