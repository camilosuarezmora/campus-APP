import json

with open("datos//campers.json", "r+") as yeison_notas:#abre el json para utilizarlo
    yeison_notas_modificable = json.load(yeison_notas) #convierte el json en diccionario que se puede modificar en py
    yeison_notas.close()
    
def nota_de_ingreso ():
    doc_camper = input("Ingresa el documento de identidad del camper \n>>")
    for dentro_del_yeison in yeison_notas_modificable:
        for mas_dentro_del_yeison in dentro_del_yeison:
            if doc_camper == mas_dentro_del_yeison:
                nota_del_camper = int(input("Ingresa la nota que quieres registrar \n >>"))
                dentro_del_yeison[doc_camper]["notaPruebaIngreso"]= nota_del_camper
                print("           REGISTRO EXITOSO           ")
                
            else:
                print("EL CAMPER NO ESTÁ REGISTRADO")
        print("==========================================")        

def guardar_campers():
    with open("datos/campers.json", "w") as yeison_notas:
        json.dump(yeison_notas_modificable, yeison_notas, indent=4)

with open("datos//notas_por_modulo.json", "r+") as yeison_notas:#abre el json para utilizarlo
    yeison_notas_modificable = json.load(yeison_notas) #convierte el json en diccionario que se puede modificar en py
    yeison_notas.close()
    
def nota_por_modulo():
    doc_camper = input("     Ingresa el documento de identidad del camper \n>>")
    for dicc_de_usuarios in yeison_notas_modificable:
        for usuario in dicc_de_usuarios:
            if doc_camper == usuario:
                skill = input("     ¿A cual skill quieres atribuir la nota? \n>>")
                skill.upper()
                nota = int(input("     Ingresa la nota que el camper sacó en esa skill  \n>>"))
                dicc_de_usuarios[doc_camper][skill]= nota
                
                #SI NO EXISTE LA SKILL LA CREA, ESO NO PUEDE SER 
                
                print("           NOTA REGISTRADA EXITOSAMENTE           ")
                print("===============================================")
    return yeison_notas_modificable

def guardar_notas():
    with open("datos/notas_por_modulo.json", "w") as yeison_notas:
        json.dump(yeison_notas_modificable, yeison_notas, indent=4)

while True:   
    print("======= ESTAS EN EL APARTADO PARA REGISTRAR NOTAS =======")
    elecc_submenu = int(input("     Escribe 1 para registrar la nota de la prueba de ingreso \n     Escribe 2 para registrar las notas de los otros modulos \n     Escribe 3 para salir \n>>"))

    if elecc_submenu == 3:
        print("               SALIDA EXITOSA               ")
        break
    elif elecc_submenu == 1:
        nota_de_ingreso()
        guardar_campers()
    elif elecc_submenu == 2:
        nota_por_modulo()  
        guardar_notas()
        
        
    