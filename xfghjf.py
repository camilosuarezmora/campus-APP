"""import json

r = ["1. para elegir a juan marino como profesor","2. para elegir a karen garcia como profesor","1. para elegir a jorge melo como profesor"]



car = "u2"
with open("datos/grupos.json")as file:
    nte = json.load(file)

while True:
    for i in r:
        print(i)
    print("seleccione una opccion")
    ig = int(input("->"))
    if ig == 1:
        nte[car]["trainer"] = "juan marino"
        break
    elif ig == 2:
        nte[car]["trainer"] = "karen garcia"
        break
    elif ig == 3:
        nte[car]["trainer"] = "jorge melo"
        break
    else:
        print("codigo no valido")
contenido = json.dumps(nte, indent=4)
with open("datos/grupos.json", "w") as file:
    file.write(contenido)""""""
