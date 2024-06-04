import json

def carga_datos(rutaArchivo):
    try:
        with open(rutaArchivo,"r") as alias:
            return json.load(alias)
    except Exception:
        print("ERROR AL CARGAR DATOS")

def guardar_datos(rutaArchivo, archivos_a_subir):
    try:
        with open(rutaArchivo, "w") as alias:
            json.dump(archivos_a_subir, alias, indent="4")
    except Exception:
        print("ERROR AL GUARDAR DATOS")                