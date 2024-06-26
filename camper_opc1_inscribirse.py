import json

def inscribirse():
    global doc
    nuevo_camper = {}
    print("========== INGRESASTE AL APARTADO REGISTROS ==========")
    print("Para registrarte sigue los pasos: ")
    
    doc = input("     Escribe aquí tu documento de identidad >> ")
    nuevo_camper["Nombre"] = input("     Escribe aquí exclusivamente tu nombre >> ")
    nuevo_camper["Apellidos"] = input("     Escribe aquí tus apellidos >> ")
    nuevo_camper["Direccion"] = input("     Escribe aquí tu dirección de residencia >> ")
    nuevo_camper["Celular"] = input("     Escribe aquí el número de tu teléfono móvil >> ")
    nuevo_camper["Fijo"] = input("     Escribe aquí el número de tu teléfono fijo >> ")
    nuevo_camper["Acudiente"] = input("     Escribe el nombre completo de tu acudiente >> ")

    nuevo_camper["Riesgo"] = False
    nuevo_camper["Estado"] = "Inscrito"
    nuevo_camper["Nota_de_ingreso"] = 0

    return nuevo_camper

try:
    nuevo_camper = inscribirse()

    with open("datos/campers.json", "r") as campers_cargados:
        campers_data = json.load(campers_cargados)

    campers_data[doc] = nuevo_camper   

    with open("datos//campers.json","w") as campers_reescritos:
        json.dump(campers_data, campers_reescritos, indent=4)
        
except Exception:
    print("Ocurrió un error")

with open("datos//notas_por_modulo.json", "r") as carga_notas:
    notas_modificable = json.load(carga_notas)
notas_modificable[doc]={}
with open("datos//notas_por_modulo.json", "w") as escribe_notas:
    json.dump(notas_modificable, escribe_notas, indent=4)


