while True:
    try:
        print("========== INGRESASTE COMO COORDINADOR ==========")
        tupla_menu_principal_coor = (
            "       Escribe 1 para registrar notas de los campers.",
            # Submenu para registrar notas de módulo e inicio
            "       Escribe 2 para cambiar el estado de un camper.",
            "       Escribe 3 para mostrar los campers con bajo rendimiento",
            "       Escribe 4 para crear una nueva ruta",
            "       Escribe 5 para ingresar al módulo de reportes.",
            # Submenu para listar los que pasaron y los que perdieron
            "       Escribe 6 para mostrar los trainers contratados.",
            "       Escribe 7 para buscar los campers y trainers que se encuentran en esa ruta",
            "       Escribe 8 para conocer los estudiantes que pasaron y que perdieron cada módulo",
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
            import coor_opc3_bajoRendimiento
        else:
            print("Opción no válida. Intente de nuevo.")
    except Exception:
        print("Ocurrió un error:")
