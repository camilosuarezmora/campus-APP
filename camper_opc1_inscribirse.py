import json

def inscribirse():
    global doc
    nuevo_camper={}
    print("========== INGRESASTE AL APARTADO REGISTROS ==========")
    print("Para registrarte sigue los pasos: ")
    
    doc = input("     Escribe aquí tu documento de identidad >> ")
    nuevo_camper["Nombre"] = input("     Escribe aquí exclusivamente tu nombre >> ")
    nuevo_camper["Apellidos"] = input("     Escribe aquí tus apellidos >> ")
    nuevo_camper["Direccion"] = input("     Escribe aquí tu dirección de residencia >> ")
    nuevo_camper["Celular"] = input("     Escribe aquí el número de tu telefono movil >> ")
    nuevo_camper["Fijo"] = input("     Escribe aquí el número de tu telefono fijo >> ")
    nuevo_camper["Acudiente"] = input("     Escribe el nombre completo de tu acudiente >> ")

    nuevo_camper["Riesgo"] = False
    nuevo_camper["Estado"] = "Inscrito"
    nuevo_camper["Nota de ingreso"] = 0

    return nuevo_camper

nuevo_camper = inscribirse()

with open("datos/campers.json", "r") as campers_cargados:
    campers_data = json.load(campers_cargados)

campers_data[doc] = nuevo_camper   

with open("datos//campers.json","w") as campers_reescritos:
       json.dump(campers_data, campers_reescritos, indent=4)
   