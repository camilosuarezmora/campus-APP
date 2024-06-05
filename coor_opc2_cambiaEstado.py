import json

print("===== INGRESASTE AL APARTADO PARA CAMBIAR EL ESTADO DE UN CAMPER =====")
doc = input("     Escribe el documento de identidad del camper \n>>")

with open("datos//campers.json", "+r") as yeison_campers:
    ysn_campers_trabajable = json.load(yeison_campers)
    
for menosUnaCapa in ysn_campers_trabajable:    
    for camper in menosUnaCapa:
        if camper == doc:
            print("Te recuerdo las opciones que tienes para cambiar el estado:\n     -INSCRITO. \n     -LISTA DE ESPERA. \n     -INGRESADO. \n     -CURSANDO.\n     -GRADUADO.\n     -EXPULSADO.\n     -RETIRADO.")
            estado = input("     Ingresa el estado que quieres que tenga el camper \n>>")
            estado.upper()
            menosUnaCapa[doc]["Estado"] = estado

with open("datos/campers.json", "w") as yeison_campers:
        json.dump(ysn_campers_trabajable, yeison_campers, indent=4)   

print("CAMBIO DE ESTADO EFECTUADO EXITOSAMENTE")
print("===================================")                 
                 