import json

try:
    print("========== CONOCE LOS CAMPERS INSCRITOS ==========")

    try:
        with open("datos//campers.json", "r") as campers:
            campers_manejable = json.load(campers)
    except FileNotFoundError:
        print("Error: El archivo 'campers.json' no se encuentra.")
        campers_manejable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'campers.json'.")
        campers_manejable = {}

    if campers_manejable:
        for doc, dicc_info in campers_manejable.items():
            try:
                nombre = dicc_info["Nombre"]
                apellidos = dicc_info["Apellidos"]
                estado = dicc_info["Estado"]

                if estado == "Inscrito":
                    print(f"    El usuario {nombre} {apellidos} con el documento {doc} se encuentra inscrito.")
            except KeyError as e:
                print(f"Error: Falta la clave {e} en los datos del camper con documento {doc}.")
            except TypeError:
                print(f"Error: Formato de datos incorrecto para el camper con documento {doc}.")
    else:
        print("No se encontraron datos en 'campers.json'.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
