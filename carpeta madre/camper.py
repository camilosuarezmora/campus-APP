mini_menu_camper = (
    "   Escribe 1 para inscribirte por primera vez.",
    "   Escribe 2 para presentar la prueba de ingreso.",
    "   Escribe 3 para ver tus notas."
)

for i in mini_menu_camper:
    print(i)

# usuarioSolito = {
#     doc: {        "Nombre" : nombre,
#         "Apellidos" :apellidos,
#         "Documento": doc,
#         "Dirección": direccion,
#         "Telefono" : cel,
#         "Acudiente" : acudiente,

#         "Riesgo": False,
#         "Estado": "Inscrito"
#     }
# }


def inscribirse():
    print("         INGRESASTE AL APARTADO REGISTROS          ")
    print("Para registrarte sigue los pasos: ")
    
    doc = input("   Escribe aquí tu documento de identidad >>")
    info_cada_camper={}
    # info_cada_camper[doc] = 
    nombre = input("    Escribe aquí tu nombre >>")

    apellido = input("     Escribe aquí tus apellidos >>")
    
    direccion = input("     Escribe aquí tu dirección de residencia >>")
    cel = input("    Escribe aquí tu telefono")
    acudiente = input("    Escribe el nombre de tu acudiente >>")

elecc_mini_menu_camper = int(input(">>"))
if elecc_mini_menu_camper == 1:
    inscribirse()

