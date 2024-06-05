#importar el txt del inicio (logo y menú principal)
with open("menu_inicial.txt", "r") as inicio:
    print(inicio.read())
    inicio.close()





while True:
    try:
        elecc_menu_cargo = int(input(">> "))
        if elecc_menu_cargo == 4:
            print("SALIDA EXITOSA")
            break
        elif elecc_menu_cargo == 1:
            import camper
        elif elecc_menu_cargo == 2:
            print("Elegiste continuar como TRAINER")
        elif elecc_menu_cargo == 3:
            import coordinacion
        else:
            print("Opción no válida. Intente de nuevo.")
    except Exception :
        print("Ocurrió un error:")

