import json

try:
    print("======= INGRESASTE A CREAR RUTAS =======")

    try:
        with open("datos//rutas.json", "r") as rutas:
            rutas_manejable = json.load(rutas)
    except FileNotFoundError:
        print("Error: El archivo 'rutas.json' no se encuentra.")
        rutas_manejable = {}
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo 'rutas.json'.")
        rutas_manejable = {}

    nombre = input("    Ingresa el nombre de la ruta que deseas crear. \n>>")

    salones = []
    while True:
        dicc = {}
        elecc_profe = input("     Ingresa 1 para atribuirle esta nueva ruta a Juan Mariño. \n     Ingresa 2 para atribuirle esta nueva ruta a Jholver.\n     Ingresa 3 para atribuirle esta nueva ruta a Miguel.\n     Ingresa 4 para dejar de agregar profesores.\n>> ")

        if elecc_profe == "4":
            print("SALIDA EXITOSA")
            break

        elif elecc_profe in ["1", "2", "3"]:
            curso = input("     Ingresa el curso que hará parte esta ruta nueva.\n>>")
            if nombre not in rutas_manejable:
                rutas_manejable[nombre] = {}

            salones.append(curso)

            if elecc_profe == "1":
                profe = "Juan Mariño"
            elif elecc_profe == "2":
                profe = "Jholver"
            elif elecc_profe == "3":
                profe = "Miguel"

            dicc[profe] = salones
            rutas_manejable[nombre] = dicc
            print("====== RUTA CREADA CON EXITO ======")

            try:
                with open("datos//rutas.json", "w") as yeison_rutas:
                    json.dump(rutas_manejable, yeison_rutas, indent=4)
            except Exception as e:
                print(f"Error al guardar los datos en 'rutas.json': {e}")

        else:
            print("Opción no válida. Por favor, ingresa una opción correcta.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

        
        # 
        
        
    


    


# with open("datos//rutas.json") as rutaas:
#     json.dump(rutas_manejable, rutaas,indent=4)
        
    #importar ruta.json para agregarle archivo
    #pedirle que pofesor va a ejercer esa ruta