def todo():
    import C_opc1_registraNotas as opc1
    import C_opc2_cambiaEstado as opc2

    while True:
        print("========== INGRESASTE COMO COORDINADOR ==========")
        tupla_menu_principal_coor = (
            "       Escribe 1 para registrar notas de los campers.",
                        #submenu para registrar notas de modulo y de inicio
            "       Escribe 2 para cambiar el estado de un camper.",
            "       Escribe 3 para crear una nueva ruta",
            "       Escribe 4 para mostrar los campers con bajo rendimiento",
            "       Escribe 5 para ingresar al modulo de reportes.",
                        #
            "       Escribe 6 para mostrar los trainers contratados.",
            "       Escribe 7 para buscar los campers y trainers que se encuentran en esa ruta",
            "       Escribe 8 para conocer los estudiantes que pasaron y que perdieron cada modulo",
                        #submenu para istar los que pasaron y los que perdieron    
            "       Escribe 9 para salir. "                    
            )

        for i in tupla_menu_principal_coor:
            print(i)
            
        eleccion_menu_principal_coor = int(input(">>"))
        
        if eleccion_menu_principal_coor == len(tupla_menu_principal_coor):
            print("               SALIDA EXITOSA               ")
            break
        elif eleccion_menu_principal_coor == 1:
            opc1.todo()
        elif eleccion_menu_principal_coor == 2:
            opc2.todo()   