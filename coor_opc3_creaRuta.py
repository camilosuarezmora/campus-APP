import json
print("======= INGRESASTE A CREAR RUTAS =======")

with open("datos//rutas.json") as rutas:
    rutas_manejable = json.load(rutas)
    
nombre = input("    Ingresa el nombre de la ruta que deseas crear. \n>>")

salones=[]
while True:
    dicc={}
    elecc_profe = input("     Ingresa 1 para atribuirle esta nueva ruta a juan mariño. \n     Ingresa 2 para atribuirle esta nueva ruta a Jholver.\n     Ingresa 3 para atribuirle esta nueva ruta a Miguel.\n     Ingresa 4 para dejar de agregar profesores.\n>> ")
    
    
    if elecc_profe == "4":
        print("SALIDA EXITOSA")
        break
    elif elecc_profe == "1":
        curso = input("     Ingresa el curso que hará parte esta ruta nueva.\n>>")
        rutas_manejable[nombre]={}
        
        salones.append(curso)
        # rutas_manejable[nombre]="Juan Mariño"
        dicc["Juan Mariño"] = salones
        rutas_manejable[nombre] = dicc
        print(rutas_manejable)
    elif elecc_profe == "2":
        curso = input("     Ingresa el curso que hará parte esta ruta nueva.\n>>")
        rutas_manejable[nombre]={}
        
        salones.append(curso)
        # rutas_manejable[nombre]="Juan Mariño"
        dicc["Jholver"] = salones
        rutas_manejable[nombre] = dicc
        print(rutas_manejable)
    elif elecc_profe == "3": 
        curso = input("     Ingresa el curso que hará parte esta ruta nueva.\n>>")
        rutas_manejable[nombre]={}
        
        salones.append(curso)
        # rutas_manejable[nombre]="Juan Mariño"
        dicc["Miguel"] = salones
        rutas_manejable[nombre] = dicc
        print(rutas_manejable)       
        
    
    with open("datos//rutas.json","w") as yeison_rutas:
        json.dump(rutas_manejable, yeison_rutas, indent=4)
    
        
        # 
        
        
    


    


# with open("datos//rutas.json") as rutaas:
#     json.dump(rutas_manejable, rutaas,indent=4)
        
    #importar ruta.json para agregarle archivo
    #pedirle que pofesor va a ejercer esa ruta