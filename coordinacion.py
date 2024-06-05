while True:
    try:
        print("========== INGRESASTE COMO COORDINADOR ==========")
        tupla_menu_principal_coor = (
            "       Escribe 1 para registrar notas de los campers.",
            "       Escribe 2 para cambiar el estado de un camper.",
            "       Escribe 3 para crear una nueva ruta",
            "       Escribe 4 para ingresar al módulo de reportes.",
                        #Listar los campers que se encuentren en estado de inscrito.
                        #Listar los campers que aprobaron el examen inicial.
                        #Listar los entrenadores que se encuentran trabajando con CampusLands.
                        #Listar los campers que cuentan con bajo rendimiento.
                        #Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.
                        #Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
            "       Escribe 9 para salir."
        )

        for i in tupla_menu_principal_coor:
            print(i)

        eleccion_menu_principal_coor = int(input(">> "))

        if eleccion_menu_principal_coor == len(tupla_menu_principal_coor):
            print("SALIDA EXITOSA")
            break
        elif eleccion_menu_principal_coor == 1:
            import coor_opc1_registraNotas
        elif eleccion_menu_principal_coor == 2:
            import coor_opc2_cambiaEstado
        elif eleccion_menu_principal_coor == 3:
            import coor_opc3_creaRuta    
        elif eleccion_menu_principal_coor == 4:
            import moduloReportes    
        else:
            print("Opción no válida. Intente de nuevo.")
    except Exception:
        print("Ocurrió un error")
