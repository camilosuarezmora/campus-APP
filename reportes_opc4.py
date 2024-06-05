import json

#try:
print("     INGRESASTE AL APARTADO 'CAMPERS DE BAJO RENDIMIENTO'   ")

with open("datos//notas_por_modulo.json", "r") as notas_de_campers:
    notas_modificable = json.load(notas_de_campers)
    
print("Campers con bajo rendimiento:")
for llave, dicc_notas in notas_modificable.items():
    for skill in dicc_notas:
        if dicc_notas[skill] is not None:
            if dicc_notas[skill] < 60: 
                print(f"    *El camper {llave} obtuvo la nota {dicc_notas[skill]} en el modulo {skill}")
print("==================================================")        
#except Exception:
#    print("Ocurrió un error")
