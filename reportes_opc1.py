import json
print("==========CONOCE LOS CAMPERS INSCRITOS==========")
 
with open("datos//campers.json","r") as campers:
    campers_manejable = json.load(campers)
    
for doc, dicc_info in campers_manejable.items():
    nombre = campers_manejable[doc]["Nombre"]
    apellidos = campers_manejable[doc]["Apellidos"]
    if campers_manejable[doc]["Estado"] == "Inscrito":
        print(f"    El usuario {nombre} {apellidos} con el documento {doc} se encuentra inscrito.")    