import json

def inscribirse():
    nuevo_camper={}
    print("********** INGRESASTE AL APARTADO REGISTROS **********")
    print("Para registrarte sigue los pasos: ")
    
    doc = input("     Escribe aquí tu documento de identidad >> ")
    nuevo_camper[doc] = {}
    nuevo_camper[doc]["Nombre"] = input("     Escribe aquí exclusivamente tu nombre >> ")
    nuevo_camper[doc]["Apellidos"] = input("     Escribe aquí tus apellidos >> ")
    nuevo_camper[doc]["Direccion"] = input("     Escribe aquí tu dirección de residencia >> ")
    nuevo_camper[doc]["Celular"] = input("     Escribe aquí el número de tu telefono movil >> ")
    nuevo_camper[doc]["Fijo"] = input("     Escribe aquí el número de tu telefono fijo >> ")
    nuevo_camper[doc]["Acudiente"] = input("     Escribe el nombre completo de tu acudiente >> ")

    nuevo_camper[doc]["Riesgo"] = False
    nuevo_camper[doc]["Estado"] = "Inscrito"
    nuevo_camper[doc]["Nota de ingreso"] = 0

    return nuevo_camper

nuevo_camper = inscribirse()

with open("datos//campers.json", "r+") as yeison_campers: #abre el json para utilizarlo
    yeison_campers_escribiendo = json.load(yeison_campers) #convierte el json en diccionario que se puede modificar en py
    yeison_campers_escribiendo.append(nuevo_camper) #al diccionario original de json se le agrega el elemento dentro de la función
    yeison_campers.seek(0)
    json.dump(yeison_campers_escribiendo, yeison_campers)
    yeison_campers.truncate()
    yeison_campers.close()