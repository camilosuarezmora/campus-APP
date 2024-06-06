import json

try:
    print("     INGRESASTE AL APARTADO 'CAMPERS DE BAJO RENDIMIENTO'   ")

    try:
        with open("datos//notas_por_modulo.json", "r") as notas_de_campers:
            notas_modificable = json.load(notas_de_campers)
    except FileNotFoundError:
        print("Error: El archivo 'notas_por_modulo.json' no se encuentra.")
        notas_modificable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'notas_por_modulo.json'.")
        notas_modificable = {}

    if notas_modificable:
        print("Campers con bajo rendimiento:")
        for llave, dicc_notas in notas_modificable.items():
            for skill in dicc_notas:
                if dicc_notas[skill] is not None:
                    if dicc_notas[skill] < 60: 
                        print(f"    *El camper {llave} obtuvo la nota {dicc_notas[skill]} en el modulo {skill}")
        print("==================================================")
    else:
        print("No se encontraron datos en 'notas_por_modulo.json'.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

