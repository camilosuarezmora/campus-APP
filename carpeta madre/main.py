#importar el txt del inicio (logo y menú principal)
inicio = open("carpeta madre//menu inicial.txt")
print(inicio.read())
inicio.close()

#importar lo de cada persona

#opcion principal
elecc_menu_cargo = int(input(">>"))


if elecc_menu_cargo == 1:
    import camper
    camper.inscribirse()
elif elecc_menu_cargo == 2:
        print("Elegiste continuar como TRAINER")
elif elecc_menu_cargo == 3:
        print("Elegiste continuar como COORDINADOR")


