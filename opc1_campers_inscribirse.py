from maneja_jsons import *


def inscribirse():
    nuevo_camper={}
    print("========== INGRESASTE AL APARTADO REGISTROS ==========")
    print("Para registrarte sigue los pasos: ")
    
    doc = input("     Escribe aquí tu documento de identidad >> ")
    nuevo_camper[doc] = {}
    nuevo_camper[doc]["Nombre"] = input("     Escribe aquí exclusivamente tu nombre >> ")
    nuevo_camper[doc]["Apellidos"] = input("     Escribe aquí tus apellidos >> ")
    nuevo_camper[doc]["Direccion"] = input("     Escribe aquí tu dirección de residencia >> ")
    nuevo_camper[doc]["Celular"] = input("     Escribe aquí el número de tu telefono movil >> ")
    nuevo_camper[doc]["Fijo"] = input("     Escribe aquí el número de tu telefono fijo >> ")
    nuevo_camper[doc]["Acudiente"] = input("     Escribe el nombre completo de tu acudiente >> ")

    nuevo_camper[doc]["Riesgo"] = False
    nuevo_camper[doc]["Estado"] = "Inscrito"
    nuevo_camper[doc]["Nota de ingreso"] = 0

    return nuevo_camper
\
def funcion_inscripcion(): 

    nuevo_camper = inscribirse()

# Cargar datos existentes
    ruta_campers = "datos\campers.json"
    datos_campers = carga_datos(ruta_campers)

    # Agregar nuevo camper a los datos existentes
    datos_campers.update(nuevo_camper)

    # Guardar datos actualizados
    guardar_datos(datos_campers, ruta_campers)

