import sys
import os

# Obtener el directorio actual (donde está camper.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Añadir el directorio actual a sys.path
sys.path.append(current_dir)

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
        from opc1_inscribirse import *
        print("=========== Usuario registrado exitosamente ===========")   
    elif elecc_mini_menu_camper == 2:
        from opc2_notas import *    
        
        

