print("========== INGRESASTE COMO CAMPER ==========")

# Tupla para mostrar las opciones dentro de "camper"
mini_menu_camper = (
    "   Escribe 1 para inscribirte por primera vez.",
    "   Escribe 2 para ver tus notas de módulo",
    "   Escribe 3 para salir."
)

try:
    while True: 
        for i in mini_menu_camper:
            print(i)

        elecc_mini_menu_camper = int(input(">>")) # Pide al usuario la elección que hizo en el primer menú de campers
        
        if elecc_mini_menu_camper == len(mini_menu_camper):
            print("               SALIDA EXITOSA               ")
            break
        elif elecc_mini_menu_camper == 1:
            import camper_opc1_inscribirse 
            print("=========== Usuario registrado exitosamente ===========")   
        elif elecc_mini_menu_camper == 2:
            import camper_opc2_notas  

except Exception:
    print("Ocurrió un error")

        
        

