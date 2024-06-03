#importar el txt del inicio (logo y menú principal)
inicio = open("menu inicial.txt")
print(inicio.read())
inicio.close()



#opcion principal
elecc_menu_cargo = int(input(">>"))

while True:
        if elecc_menu_cargo == 4:
                print("               SALIDA EXITOSA               ")
                break
        elif elecc_menu_cargo == 1:
                from campers import camper
        elif elecc_menu_cargo == 2:
                print("Elegiste continuar como TRAINER")
        elif elecc_menu_cargo == 3:
                print("Elegiste continuar como COORDINADOR")


