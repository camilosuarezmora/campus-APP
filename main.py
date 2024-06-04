#importar el txt del inicio (logo y menú principal)
import camper 
import C_main_de_coordinacion 
import maneja_jsons as maneja_jsons 

inicio = open("menu inicial.txt")
print(inicio.read())
inicio.close()

ruta_campers="datos//campers.json"
datos_campers=maneja_jsons.carga_datos(ruta_campers)


#opcion principal
elecc_menu_cargo = int(input(">>"))

while True:
        if elecc_menu_cargo == 4:
                print("               SALIDA EXITOSA               ")
                break
        elif elecc_menu_cargo == 1:
                camper.funcion_ejemplo()
        elif elecc_menu_cargo == 2:
                print("Elegiste continuar como TRAINER")
        elif elecc_menu_cargo == 3:
                C_main_de_coordinacion.todo()


maneja_jsons.guardar_datos(ruta_campers,datos_campers)