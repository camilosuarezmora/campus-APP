tuplaReportes = (
        "       Ingresa 1 para listar los campers que se encuentren en estado de inscrito.",
        "       Ingresa 2 para listar los campers que aprobaron el examen inicial.",
        "       Ingresa 3 para listar los entrenadores que se encuentran trabajando con CampusLands.",
        "       Ingresa 4 para listar los campers que cuentan con bajo rendimiento.",
        "       Ingresa 5 para listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.",
        "       Ingresa 6 para mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.",
        "       Ingresa 7 para SALIR"
    )

while True:
    print("=======INGRESASTE AL MODULO DE REPORTES========")
    
    for i in tuplaReportes:
        print(i)

    try:
        selecc = int(input(">>"))  

        if selecc == len(tuplaReportes):
            print("     SALIDA EXITOSA     ")
            break
        elif selecc == 1:
            import reportes_opc1
        elif selecc == 2:
            import reportes_opc2
        elif selecc == 3:
            import reportes_opc3
        elif selecc == 4:
            import reportes_opc4
        elif selecc == 5:
            import reportes_opc5
        elif selecc == 6:
            print("Pendiente")  
        else:
            print("ERROR, VUELVE A INTENTAR") 
    except Exception:
        print("Hubo un error, vuelve a intentar")                             