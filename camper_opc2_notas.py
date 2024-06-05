import json

print("============ INGRESASTE A LA SECCION DE VER NOTAS ============")

doc = input("     Ingresa tu documento de identidad     \n>>")

try:
    with open("datos//notas_por_modulo.json", "r+") as yeison_notas:
        yeison_notas_modificable = json.load(yeison_notas)

        for dicc_de_usuarios in yeison_notas_modificable:
            for documentos in dicc_de_usuarios:
                   
                if doc == documentos:   
                    for notas_y_modulo in dicc_de_usuarios.values():
                        for key, value in notas_y_modulo.items():
                            print(f"Tu nota en {key} fue: {value}")
    print("==================================================")
                
except Exception:
    print("Ocurrió un error")
