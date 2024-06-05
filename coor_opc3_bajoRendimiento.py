import json

try:
    print("     INGRESASTE AL APARTADO 'CAMPERS DE BAJO RENDIMIENTO'   ")

    with open("datos//notas_por_modulo.json", "r") as notas_de_campers:
        notas_modificable = json.load(notas_de_campers)

    for campers in notas_modificable:
        for info_camper in campers:
            print("pendiente")
    
    print("==================================================")        
except Exception:
    print("Ocurrió un error:")
