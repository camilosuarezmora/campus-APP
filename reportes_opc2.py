import json

try:
    print("     CONOCE LOS CAMPERS QUE APROBARON LA PRUEBA DE INGRESO   ")

    try:
        with open("datos//campers.json", "r") as campers:
            manejable = json.load(campers)
    except FileNotFoundError:
        print("Error: El archivo 'campers.json' no se encuentra.")
        manejable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'campers.json'.")
        manejable = {}

    aprobaron = []
    aprobo = False

    if manejable:
        for contenido in manejable:
            try:
                nota = manejable[contenido]["Nota_de_ingreso"]
                nombre = manejable[contenido]["Nombre"]
                if nota > 60:
                    aprobo = True
                    aprobaron.append((nombre, contenido, nota))
            except KeyError as e:
                print(f"Error: Falta la clave {e} en los datos del camper con documento {contenido}.")
            except TypeError:
                print(f"Error: Formato de datos incorrecto para el camper con documento {contenido}.")

        if aprobo:
            for nombre, contenido, nota in aprobaron:
                print(f"El usuario {nombre} con el documento {contenido} aprobó la prueba de ingreso con una nota de {nota}")
        else:
            print("Ningún camper aprobó la prueba de ingreso.")
    else:
        print("No se encontraron datos en 'campers.json'.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
