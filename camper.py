import opc1_campers_inscribirse as opc1_campers_inscribirse 
import opc2_campers_notas as opc2_campers_notas 

def funcion_ejemplo():
    print("========== INGRESASTE COMO CAMPER ==========")

    #tupla para mostrar las opciones dentro de "camper"
    mini_menu_camper = (
        "   Escribe 1 para inscribirte por primera vez.",
        "   Escribe 2 para ver tus notas de modulo",
        "   Escribe 3 para salir."
    )

    while True: 
        for i in mini_menu_camper:
            print(i)

        elecc_mini_menu_camper = int(input(">>")) #pide al usuario la elección que hizo en el primer menú de campers
        
        if elecc_mini_menu_camper == len(mini_menu_camper):
            print("               SALIDA EXITOSA               ")
            break
        elif elecc_mini_menu_camper == 1:
            opc1_campers_inscribirse.funcion_inscripcion()
            print("=========== Usuario registrado exitosamente ===========")   
        elif elecc_mini_menu_camper == 2:
            opc2_campers_notas.funcion_vernotas()
        
        

